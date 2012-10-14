from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tracker.views',
	url(r'^challenges/$', 'challengeindex'),
	url(r'^challenge/(?P<id>-?\d+)/$', 'challenge'),
	url(r'^choices/$', 'choiceindex'),
	url(r'^choice/(?P<id>-?\d+)/$', 'choice'),
	url(r'^choiceoption/(?P<id>-?\d+)/$', 'choiceoption'),
	url(r'^choicebid/add/(?P<id>-?\d+)/$', 'choicebidadd'),
	url(r'^donors/$', 'donorindex'),
	url(r'^donor/(?P<id>-?\d+)/$', 'donor'),
	url(r'^donations/$', 'donationindex'),
	url(r'^donation/(?P<id>-?\d+)/$', 'donation'),
	url(r'^runs/$', 'runindex'),
	url(r'^run/(?P<id>-?\d+)/$', 'run'),
	url(r'^prizes/$', 'prizeindex'),
	url(r'^prize/(?P<id>-?\d+)/$', 'prize'),
	url(r'^chipin/$', 'chipin_action'),
	url(r'^events/$', 'eventlist'),
	url(r'^setusername/$', 'setusername'),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^search/$', 'search'),
	url(r'^index/$', 'index'),
	url(r'^$', 'index'),
)