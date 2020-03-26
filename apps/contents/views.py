from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.bookinfo.models import libray


# class indexView(View):
#     def get(self,request):
#         lib=libray.objects.all()
#         print(lib)
#         return render(request,"index.html",context={"book":lib})

class dataView(View):
    def get(self,request,page):
        lib = libray.objects.all()
        paginator=Paginator(lib,10)
        book=paginator.page(page)
        return render(request, "page.html", context={"book": book,"page_num":int(page)})

