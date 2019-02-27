from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'intro.html')

def reviews(request):
    blogs = Blog.objects
    return render(request, 'reviews.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})