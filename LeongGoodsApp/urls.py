from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'list/(?P<type_id>((\d)+))/(?P<pindex>((\d)+))$', views.list, name='list'),
    url(r'deatil/(?P<good_id>((\d)+))/$', views.deatil, name='deatil'),
    url(r'cart/$', views.cart, name='cart'),
    url(r'order/$', views.order, name='order'),
    url(r'join/$', views.join_cart, name='join'),
    url(r'delete/$', views.delete_cart, name='delete'),
    # url(r'add/$',views.add,name='add'),
    # url(r'lose/$',views.lose,name='lose'),
]
