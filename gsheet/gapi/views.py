from django.shortcuts import render
from rest_framework import generics
from myapp.models import Googs


# Create your views here.
class GAPIView(generics.ListAPIView):
    queryset = Googs.objects.all()