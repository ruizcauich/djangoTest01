from django.contrib import admin
from .models import Todo
# Register your models here.
#Permmite agregar un Todo al sidio admin
admin.site.register(Todo)
