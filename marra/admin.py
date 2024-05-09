from django.contrib import admin
from .models import Contact,Blog
#register your models here.

admin.site.register((Blog,Contact))
