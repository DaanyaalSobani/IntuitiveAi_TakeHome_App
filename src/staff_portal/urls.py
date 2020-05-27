from django.contrib import admin
from django.urls import path, include
from . import views
from . import apis
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('api/organizations', apis.organizations_info),
]