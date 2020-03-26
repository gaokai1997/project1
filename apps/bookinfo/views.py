from datetime import date

from django import http
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from django.views import View

from apps.bookinfo.models import libray
from apps.users.models import User


class uploadView(View):
    def get(self,request):
        if request.user.is_superuser:
            book=libray.objects.all()
            users=User.objects.all()
            for i in users:
                # print(i)
                # print(i.date_joined,type(i.date_joined))
                i.date_joined=str(i.date_joined)
                # print(i.date_joined, type(i.date_joined))
                i.date_joined=i.date_joined.split('.')[0]

            return render(request,"guanli.html",context={'book':book,"users":users})
        else:
            return http.HttpResponse("您不是管理员")
    def post(self,request):
        id=request.POST.get("id")
        libray.objects.filter(id=id).delete()
        return redirect(reverse("bookinfo:upload"))

class deluserView(View):
    def get(self,request):
        book=libray.objects.all()
        users=User.objects.all()
        for i in users:
            print(i)
            print(i.date_joined,type(i.date_joined))
            i.date_joined=str(i.date_joined)
            print(i.date_joined, type(i.date_joined))
            i.date_joined=i.date_joined.split('.')[0]

        return render(request,"guanli.html",context={'book':book,"users":users})
    def post(self,request):
        username=request.POST.get("username")
        print(username)
        User.objects.filter(username=username).delete()
        return redirect(reverse("bookinfo:deluser"))