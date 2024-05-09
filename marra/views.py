from django.shortcuts import render
from django.contrib import messages
from .models import Blog

def home_view(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request,"index.html",context=context)
