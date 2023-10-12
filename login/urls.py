from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.home , name='account' ),
    path('signup/' , views.signup, name='signup'),
    path('login/' , views.login , name='login'),
    path('home1/' , views.home1 , name='home1'),
    path('about/' , views.about , name='about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('download-specific-field-pdf/', views.download_specific_field_pdf, name='download_specific_field_pdf'),
   
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

