from django.conf.urls import url
from .views import *
from LeongGoodsApp import urls as le_url

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^register_handle/$', register_handle),
    url(r'^login/$', login, name='login'),
    url(r'^login_handle/$', login_handle),
    url(r'^info/$', info, name='info'),
    url(r'^order/$', order, name='order'),
    url(r'^site/$', site, name='site'),
    url(r'^change/$', change_site, name='change'),
    url(r'^order_handle/$', order_handle, name='ording')
]
