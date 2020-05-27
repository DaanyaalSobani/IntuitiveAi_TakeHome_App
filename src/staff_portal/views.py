from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, RedirectView, DetailView,TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "staff_portal/index.html"
