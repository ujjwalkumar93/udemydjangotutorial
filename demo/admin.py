from django.contrib import admin
from .models import  Book
from .models import  Charecter, Auther
# Register your models here.
admin.site.register(Book)
admin.site.register(Charecter)
admin.site.register(Auther)
