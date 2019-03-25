from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^$',view=index),
    url(r'^car/$',view=carinfo,name='car'),
    url(r'^detail/$',view=detail,name='detail')
]