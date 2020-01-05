from django.conf.urls import url
from django.urls import path
from  . import views

app_name = 'work'

urlpatterns = [
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]
