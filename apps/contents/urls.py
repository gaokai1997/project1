from django.conf.urls import url, include
from django.contrib import admin

from apps.contents import views

urlpatterns = [
    # url(r'^index/$',views.indexView.as_view(),name="index"),
    url(r'index/(?P<page>\d+)/$',views.dataView.as_view(),name="index")
]