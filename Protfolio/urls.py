from django.urls import path
from Protfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
]

