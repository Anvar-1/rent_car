from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Brand


admin.site.register(Brand)

class BrandAdmin(ModelAdmin):
    pass
