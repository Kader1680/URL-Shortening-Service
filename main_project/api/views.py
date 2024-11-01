

from rest_framework.response import Response
from rest_framework.decorators import api_view 

from django.http import HttpResponse
from .models import User
from .models import Url
from .serializer import UserSerialzer
from rest_framework import status

from django.shortcuts import render

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
          obj = Url(title=url)
          obj.save()
    
    return render(request, "form.html")




@api_view(["POST"])
def storeData(request):
    serialize = UserSerialzer(data=request.data)   
    # check the serilzer data if it valid
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)
