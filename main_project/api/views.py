

from rest_framework.response import Response
from rest_framework.decorators import api_view 

from django.http import HttpResponse
# from .models import User
from .models import Url
# from .serializer import UserSerialzer
from rest_framework import status

from django.shortcuts import render, redirect
import random
import string   

# from django.contrib.auth.forms import UserCreationForm
# from .forms import InputForm
 
user_data = [{
    "id": 101,
    "name": "mellisa",
    "age": 35,
    "is_active": True,
},
             {
    "id": 101,
    "name": "irland",
    "age": 27,
    "is_active": True,
},
             {
    "id": 101,
    "name": "isabelle",
     
    "age": 30,
    "is_active": True,
},
             {
    "id": 101,
    "name": "cherry",
    "age": 31,
    "is_active": True,
},
             
             
             
             ]



@api_view(["GET"])
def getData(request):
    # user = {"name" : "abdel", "age": 25}
    # users = User.objects.all()
    return render(request, 'index.html',  {"title" : "get data"})

 
 
@api_view(["GET"])
 
def form(request):
    users = {
        'users' : user_data
    }
    return render(request, 'form.html', users)
    
@api_view(["GET"])    
def getUrls(request):
    
    allUrls = Url.objects.all()
    return render(request, "index.html",  {"allUrls" : allUrls})
    
    
def main(request):
    return HttpResponse("wiiiou")
 
def storeUrl(request):    
    if request.method == "POST":
          url = request.POST['url']
          
          slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
          new_url = Url(title=url, slug=slug)
          new_url.save()
        
          return redirect('/')
   
    return redirect('/')
     


def redirectToUrl(request, slug):
   return "dff"      
 
 
def edit(request, pk):
    obj = Url.objects.get(pk = pk)
    if request.method == "POST":
        
        obj.title = request.POST['url']
        obj.save()
    
    obj = Url.objects.get(pk=pk)
    context = {"obj":obj}
    return render(request, "edit.html", context)


def delete(request, pk):
    obj = Url.objects.get(pk = pk)
    if request.method == "POST":
       obj.delete()
       return HttpResponse("delete the url")
   
    return HttpResponse("delete the url")
    
# @api_view(["POST"])
# def storeData(request):
#     serialize = UserSerialzer(data=request.data)   
#     # check the serilzer data if it valid
#     if serialize.is_valid():
#         serialize.save()
#         return Response(serialize.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(status=status.HTTP_400_BAD_REQUEST)


# authentication Part

# def login(request):
    
#     return render(request, "login.html")
 

# def register(request):
    
#     # if request.method == "POST":
#     #    username = request.POST['username']
#     #    email = request.POST['email']
#     #    passowrd = request.POST['passowrd']
#     #    data = User(username=username, email=email, passowrd=passowrd)
#     #    data.save()
    
#     # return render(request, "register.html")
    
#     form = UserCreationForm()
    
#     return render(request, "register.html", {"form": form})
#     # context ={}
#     # context['form']= InputForm()
#     # return render(request, "home.html", context)