from django.shortcuts import render
from rest_framework import generics, serializers
from myapp.models import Googs
from .serializers import SheetSerializer


class GAPIView(generics.ListAPIView):
    queryset = Googs.objects.all()
    serializer_class = SheetSerializer