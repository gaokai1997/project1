from django import http
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from apps.users.models import User


class registerView(View):
    def get(self,request):
        return render(request,"zhuce1.html")
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        mobile=request.POST.get("mobile")
        User.objects.create_user(username=username,password=password,mobile=mobile)
        return redirect(reverse("users:login"))
class loginView(View):
    def get(self,request):
        return render(request, "denglu.html")
    def post(self,request):
        username=request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            return http.HttpResponse("用户名或者密码错误")
        else:
            login(request,user)
            request.session.set_expiry(None)
            response=redirect("index/1")
            # response.set_cookie("username",user.username,max_age=3600*24*14)
            return response

class logoutView(View):
    def get(self,request):
        logout(request)
        response=redirect(reverse("users:login"))
        response.delete_cookie("username")
        return response


