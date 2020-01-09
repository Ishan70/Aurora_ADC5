from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from .forms import PostForm
# Create your views here.

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print (form.value)
        print ('Hello')
    form = PostForm()
    return render(request, 'createPost/create.html', context={'posts': Posts.objects.all})

def viewAll(request):
    return render(request, 'createPost/viewAll.html', context={'posts': Posts.objects.all})
