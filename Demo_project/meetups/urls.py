from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetups/<slug:meetup_slug>/', views.meetup_details, name='meetup_details'),
    path('success_page/', views.success_page, name='success_page'),
]
