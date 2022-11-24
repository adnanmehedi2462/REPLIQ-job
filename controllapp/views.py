from django.shortcuts import render
from rest_framework import generics , mixins,viewsets,views

from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics , mixins,viewsets,views
from .serializers import *
from .models import *
# Create your views here.

class allassets(ModelViewSet):
    serializer_class=AssetsTrackserializers
    queryset=Assets_management.objects.all().order_by("-id")
    

#  you can add or viwe any company    
class CompanyView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Company.objects.all().order_by("-id")
    serializer_class=CompanySerializers
    lookup_field="id"
    def get(self,request,id=None):
        
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
        
# Employee controll area    
  
class EmployeeView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all().order_by("-id")