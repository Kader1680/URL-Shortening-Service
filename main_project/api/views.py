

from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import User
from .serializer import UserSerialzer
from rest_framework import status

from django.shortcuts import render
@api_view(["GET"])
def getData(request):
    # user = {"name" : "abdel", "age": 25}
    # users = User.objects.all()
    return render(request, 'index.html')

 

@api_view(["POST"])
def storeData(request):
    serialize = UserSerialzer(data=request.data)   
    # check the serilzer data if it valid
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)
