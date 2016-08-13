from django.shortcuts import redirect

def save_uid_to_session(strategy, uid=None, **kwargs):
  if uid:
    strategy.session_set('uid', uid)
  return redirect(strategy.session_get('next'))
