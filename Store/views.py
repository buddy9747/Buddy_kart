from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Catlog,Product
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.views.generic.edit import CreateView,DeleteView,UpdateView,View
from django.urls import reverse_lazy

class Detail(DeleteView):
    model=Product
    template_name = "Store/detailview.html"
class UpdateCatlog(UpdateView):
    model = Product
    fields = ["ptitle","brand","image","price","act_price","cat_id"]
    template_name = "Store/formtemplate.html"

class DeleteCatlog(DeleteView):
    model = Product
    template_name = "Store/formtemplate.html"
    success_url = reverse_lazy("Store:addprod")



class AddCatlog(CreateView):
    model = Product
    fields = ["ptitle","brand","image","price","act_price","cat_id"]
    template_name = "Store/formtemplate.html"

def loginpage(request):
    myform=LoginForm(request.POST or None)
    if myform.is_valid():
        usern=myform.cleaned_data.get("username")
        passw=myform.cleaned_data.get("password")
        user=authenticate(username=usern,password=passw)
        if user:
            return redirect("/onbazar")
    return render(request,"Store/formtemplate.html",{"form":myform})

def fun(request):
    a=Catlog.objects.all()
    s=set([i.title for i in a])
    d={}
    for i in s:
        x = Catlog.objects.filter(title=i)
        sub = [j.category for j in x]
        d[i] = sub

    return render(request,"Store/home.html",{"menus":d})

def fun1(request,menu):
    a=Catlog.objects.get(category=menu)
    return render(request,"Store/detail.html",{"cat":a})


# Create your views here.
