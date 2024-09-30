## restaurant/urls.py
## Description: provides proper paths in order to display any possible page, also assigns nicknames for easier access

from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path(r'', views.main, name="restaurant"),
    path(r'about', views.submit, name="submit"),
    #path(r'show_all', views.confirmation, name="confirmation"),
    path(r'show_all', views.order, name="order"),
]