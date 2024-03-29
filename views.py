
from .models import Blog
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})



def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.images = request.GET['images']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def about(request):
    return render(request, 'about.html')



# Create your views here.

