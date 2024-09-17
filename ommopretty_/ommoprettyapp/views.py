from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from ommoprettyapp.models import Product
from django.db.models import Q


# Create your views here.


def home(request):
    userdata=request.user.id
    # print("UserData id:",userdata)
    # print("UserData id:",request.user.is_authenticated)
    obj=Product.objects.filter(is_active=True)
    context={'product':obj}
    return render(request,"index.html",context)


def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        c=request.POST['ucpass']
        uobj=User.objects.create(username=u,email=u)
        uobj.set_password(p)
        uobj.save()
        return redirect('/register')
   
def user_login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        a=authenticate(username=u,password=p)
        if a is not None:
            print(a)
            print(a.password,a.id)
            login(request,a)
            return redirect('/')
       
        else:
            print(a)
            return HttpResponse("Login Fail ")


def user_logout(request):
    logout(request)
    return redirect("/")

def product_detail(request,pid):
    obj=Product.objects.filter(id=pid)
    context={'product':obj}
    return render(request,"productdetail.html",context)

    
def catfilter(request,cv):
    if cv == "1":
         obj=Product.objects.filter(cat=1)
         context={'product':obj}
         return render(request,"index.html",context)
    elif cv =='2':
        obj=Product.objects.filter(cat=2)
        context={'product':obj}
        return render(request,"index.html",context)
    else:
         obj=Product.objects.filter(cat=3)
         context={'product':obj}
         return render(request,"index.html",context)
    
def range(request):
    if request.method == "GET":
        min=request.GET['min']
        max=request.GET['max']
        c1=Q(price__gte=min)
        c2=Q(price__lte=max)
        obj=Product.objects.filter(c1 & c2)
        context={'product':obj}
        return render(request,"index.html",context)
    
def about(request):
    return render(request,'about.html')

def book(request):
    return render(request,'book.html')

def bookmakeup(request):
    return render(request,'bookmakeup.html')

def contact(request):
    return render(request,'contact.html')
