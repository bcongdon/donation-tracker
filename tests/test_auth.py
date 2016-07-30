import re

from django.test import TestCase, TransactionTestCase
from django.contrib.auth import get_user_model

import post_office.models

import tracker.auth
import tracker.tests.util as test_util

from social.apps.django_app.default.models import UserSocialAuth

AuthUser = get_user_model()

TEST_AUTH_MAIL_TEMPLATE = post_office.models.EmailTemplate(content="user:{{user}}\nurl:{{reset_url}}")

class TestRegisterEmailSend(TestCase):

    def test_send_registration_email(self):
        newUser = AuthUser.objects.create(username='dummyuser',email='test@email.com',is_active=False)
        sentMail = tracker.auth.send_registration_mail('', newUser, template=TEST_AUTH_MAIL_TEMPLATE)
        contents = test_util.parse_test_mail(sentMail)
        self.assertEqual(newUser.username, contents['user'][0])
        domainURL,middle,suffix = contents['url'][0].partition('?')
        self.assertEqual(tracker.auth.make_auth_token_url_suffix(newUser), suffix)
     
    def test_send_password_reset_email(self):
        existingUser = AuthUser.objects.create(username='existinguser',email='test@email.com',is_active=True)
        sentMail = tracker.auth.send_password_reset_mail('', existingUser, template=TEST_AUTH_MAIL_TEMPLATE)
        contents = test_util.parse_test_mail(sentMail)
        self.assertEqual(existingUser.username, contents['user'][0])
        domainURL,middle,suffix = contents['url'][0].partition('?')
        self.assertEqual(tracker.auth.make_auth_token_url_suffix(existingUser), suffix)

    def test_send_registration_email_existing_user_fails(self):
        existingUser = AuthUser.objects.create(username='existinguser',email='test@email.com',is_active=True)
        self.assertRaises(Exception, tracker.auth.send_registration_mail('', existingUser, template=TEST_AUTH_MAIL_TEMPLATE))
    
    def test_send_password_reset_new_user_fails(self):
        newUser = AuthUser.objects.create(username='dummyuser',email='test@email.com',is_active=False)
        self.assertRaises(Exception, tracker.auth.send_password_reset_mail('', newUser, template=TEST_AUTH_MAIL_TEMPLATE))
    

class TestSocialAuth(TestCase):

    def test_steam_association(self):
        newUser = AuthUser.objects.create(username='dummyuser',email='test@email.com',is_active=False)
        socialAuth = UserSocialAuth.objects.create(user=newUser,provider='steam',uid='123456')
        assert newUser.social_auth.filter(provider='steam').first().uid == '123456'

    def test_no_social_auth(self):
        nonSocialUser = AuthUser.objects.create(username='dummyuser',email='test@email.com',is_active=False)
        assert nonSocialUser.social_auth.filter(provider='steam').first() == None
