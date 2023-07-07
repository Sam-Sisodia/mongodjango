from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *

from rest_framework.viewsets import ModelViewSet



class Studentdetails(ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerilizer



class Schooldetails(ModelViewSet):
    queryset = School.objects.all() 
    serializer_class = SchoolSerilizer