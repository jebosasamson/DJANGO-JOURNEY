from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('news', news, name='news'),
    path('contact', contact, name='contact'),
    path('trainer', trainer, name='trainer'),
    path('program_detail/<int:id>', program_detail, name='program_detail'),
    path('our-club', our_club, name='our-club' )
] 