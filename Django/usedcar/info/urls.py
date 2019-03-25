from django.conf.urls import url
from django.contrib import admin

from .views import *
urlpatterns=[
    url(r'^register/$',view=register,name='register'),
    url(r'^registerin/$',view=registerin,name='registerin'),
    url(r'^login/$',view=login_,name='login'),
    url(r'^loginin/$',view=loginin,name='loginin'),
    url(r'^detail/$',view=detail),
    url(r'^header/$',view=header),
    url(r'^logout/$',view=logout_),
]