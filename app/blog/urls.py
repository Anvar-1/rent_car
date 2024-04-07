from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/blogs/', BlogModelListCreateView.as_view()),
    path('api/v1/blogs/<int:pk>/', BlogUpdateView.as_view()),
    path('api/v1/blogs/delete', BlogDeleteView.as_view()),
]
