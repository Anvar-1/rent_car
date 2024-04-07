from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import BlogModelSerializer
from .models import BlogModel

class BlogModelListCreateView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer

class BlogUpdateView(RetrieveUpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer 

class BlogDeleteView(RetrieveDestroyAPIView):    
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer 
