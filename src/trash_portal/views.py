from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, RedirectView


class IndexView(LoginRequiredMixin, RedirectView):
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    url = 'portal_control'


class PortalControlView(LoginRequiredMixin, RedirectView):
    login_url = '/accounts/login'

    def get_redirect_url(self, *args, **kwargs):
        print(dir(self.request.user))
        if True:
            return '/test'
        else:
            return '/testFalse'


