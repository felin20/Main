from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView




# Create your views here.

def home(request):
    return render(request,'home.html')

def home1(request):
   return render(request,'home1.html')

def search(request):
   if 'q' in request.GET:
      q=request.GET['q']
      data=Movie.objects.filter(Moviename__icontains=q)
      data1=Criticreview.objects.filter(Critic__icontains=q)
   else:
      data=Movie.objects.all()
      data1=Criticreview.objects.all()
   return render(request,'search.html',{'data':data,'data1':data1})

def ulogin(request):
    return render(request,'ulogin.html')

def clogin(request):
   return render(request,'clogin.html')

def welcome(request):
   return render(request,'welcome.html')

def movlist(request):
    mov=Movie.objects.all()
    return render(request,'movlist.html',{'mov':mov})



def mdetail(request,Moviename):
    det=Movie.objects.get(Moviename=Moviename)
    urev=Userreview.objects.filter(Moviename=Moviename)
    crev=Criticreview.objects.filter(Moviename=Moviename)
    return render(request,'mdet.html',{'det':det,'urev':urev,'crev':crev})







def crev(request,Moviename):
   crev=Criticreview.objects.filter(Moviename=Moviename)
   return render(request,'mdet2.html',{'crev':crev})


# Create your views here.

# def register(request):
#     if request.method=='POST':
#         form=Regform(request.POST)
#         a=form.data['username']
#         if form.is_valid():
#             form.save()
            
#             return redirect(home)
#     else:

#      form=Regform()
#     return render(request,'regform.html',{'form':form})


# def register(request):
#     if request.method=='POST':
#      form=Regform(request.POST)
#      if form.is_valid():
#         s1=User(
#           username=form.cleaned_data['username'],
#           first_name=form.cleaned_data['first_name'],
#           last_name=form.cleaned_data['last_name'],
#         email=form.cleaned_data['email'],
#         password=form.cleaned_data['password'])
#         s1.save()
#         return  HttpResponseRedirect('home')
#     else:
#       form=Regform()
  
#     return render(request,'regform.html',{'form':form})

def register(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      confirm_password=request.POST['confirm_password']
      if password==confirm_password:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('reg')
         else:
            user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email,last_name=last_name)
            user.set_password(password)
            user.save()
            print('success')
            return redirect('login')
         
   else:
      print('This is not post method')
      return render(request,'regform.html')
   
def register1(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      confirm_password=request.POST['confirm_password']
      if password==confirm_password:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('reg1')
         else:
            usr=User.objects.create_user(username=username,password=password,first_name=first_name,email=email,last_name=last_name)
            usr.set_password(password)
            usr.save()
            print('success')
            return redirect('login1')
         
   else:
      print('This is not post method')
      return render(request,'regform1.html')

# def loginuser(request):
#    if request.method=='POST':
#       username=request.POST['username']
#       password=request.POST['password']

#       User=authenticate(request,username=username,password=password)
#       if User:
#          login(request,User)
#          messages.success(request,'user has been successfully logged in')
#          return redirect(home)
#    else:\\\
#       print('authentication failed')
#    return render(request,'login.html')

# def loginuser(request):
#    if request.method=='POST':
#       form=AuthenticationForm(data=request.POST)
#       if form.is_valid():
#          return redirect(welcome)
#    else:
#       form=AuthenticationForm()
#    return render(request,'login.html',{'form':form})
   
def loginuser(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']

      user=auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('home')
      else:
         messages.info(request,'Invalid Username or Password')
         return redirect('login')
      
   return render(request,'login.html')


def loginuser1(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']

      usr=auth.authenticate(username=username,password=password)

      if usr is not None:
         auth.login(request,usr)
         return redirect(home1)
      else:
         messages.info(request,'Invalid Username or Password')
         return redirect('login1')
      
   return render(request,'login1.html')


def logoutuser(request):
   logout(request)
   messages.success(request,'user has been successfully logged out')

   return redirect(home)


def home(request):
   return render(request,'home.html')

def adrev(request):
   form=revform()
   if request.POST:
      form=revform(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
       form.save()
      return redirect(home)
   else:
      form=revform()  
      return render(request,'adrev.html',{'form':form})

def adcrev(request):
   if request.POST:
      form=crevform(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
       form.save()
      return redirect(home)
   else:
      form=crevform()
      return render(request,'adcrev.html',{'form':form})

def myreview(request,Username):
 urev=Userreview.objects.filter(Username=Username)
 
 return render(request,'userreviews.html',{'urev':urev})

def mycritic(request,Criticname):
   crev=Criticreview.objects.filter(Criticname=Criticname)
   return render(request,'criticreviews.html',{'crev':crev})





# class adrev(CreateView):
#    model=Userreview
#    fields='__all__'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#    context_object_name='form'
#    template_name='adrev.html'
#    success_url='movlist'

# class editto(UpdateView):
#    model=Userreview
#    fields='__all__'
#    template_name='adrev.html'
#    success_url='movlist'

# class todelete(DeleteView):
#    model=Userreview
#    template_name='todelete.html'
#    context_object_name='c'
#    success_url='movlist'

def editto(request,id):
   edit=Userreview.objects.get(id=id)
   
   if request.method=='POST':
      form=revform(request.POST,instance=edit)
      if form.is_valid():
        form.save()
        return redirect(home)
     
   form=revform(instance=edit)
   return render(request,'editadrev.html',{'form':form,'edit':edit})

def editto1(request,id):
   edit=Criticreview.objects.get(id=id)
   
   if request.method=='POST':
      form=crevform(request.POST,instance=edit)
      if form.is_valid():
        form.save()
        return redirect(home)
     
   form=crevform(instance=edit)
   return render(request,'editadcrev.html',{'form':form,'edit':edit})




def todelete(request,id):
   td=Userreview.objects.filter(id=id)
   
   if request.method=='POST':
      td.delete()
      
      return redirect(home)
   return render(request,'todelete.html',{'td':td})

def todelete1(request,id):
   td=Criticreview.objects.filter(id=id)
   
   if request.method=='POST':
      td.delete()
      
      return redirect(home)
   return render(request,'todeletec.html',{'td':td})
   





   




