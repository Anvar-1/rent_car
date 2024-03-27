from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.brand.urls')),
    path('api/', include('app.car.urls')),
]