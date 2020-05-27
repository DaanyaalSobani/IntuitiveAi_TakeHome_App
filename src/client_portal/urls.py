from django.contrib import admin
from django.urls import path, include
from . import views
from . import apis

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('api/wastemanager', apis.wastemanager_info),
    path('api/trash', apis.trash_info)
]