from django.conf.urls import url, include
from django.contrib import admin

from apps.bookinfo import views

urlpatterns = [
    url(r'^upload/$',views.uploadView.as_view(),name="upload"),
    url(r'^deluser/$',views.deluserView.as_view(),name="deluser"),
#     url(r'^index/$',views.indexView.as_view(),name="index"),
#     url(r'index/(?P<page>\d+)/$',views.dataView.as_view(),name="data")
]