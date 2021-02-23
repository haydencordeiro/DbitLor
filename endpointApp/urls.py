
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from endpointApp import views
from rest_framework import routers
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('api/loggedinuserdetails/', views.ProfileView.as_view(),
         name='ProfileView'),

    path('api/applyforlor/', views.ApplyForLor,
         name='ApplyForLor'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
