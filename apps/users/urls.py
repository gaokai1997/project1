from django.conf.urls import url, include
from django.contrib import admin

from apps.users import views

urlpatterns = [
    url(r'^register/$',views.registerView.as_view(),name="register"),
    url(r'^login/$',views.loginView.as_view(),name="login"),
    url(r'^logout/$',views.logoutView.as_view(),name="logout"),
]