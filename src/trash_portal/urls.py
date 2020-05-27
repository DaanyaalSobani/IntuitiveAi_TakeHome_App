from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('portal_control/', views.PortalControlView.as_view()),
    path('staff/', include('staff_portal.urls')),
    path('clients/', include('client_portal.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
