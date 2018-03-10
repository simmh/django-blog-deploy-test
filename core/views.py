from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import redirect, resolve_url
from .models import Category, Post
import json

from .forms import *

import logging
logger = logging.getLogger('django')
# logger.info('the_file: %s' % the_file)

# # Create your views here.


def serve_html(request, path):
    # logger.info('path: %s' % path)

    return render(request, path)


def index(request, message=None):
    return render(request, 'index.html')



def get_category_list(request):
    data = Category.dump_bulk()
    return HttpResponse(json.dumps(data), content_type='application/json')



def post_list_view(request, category=None):
    if category:
        if category == 'all':
            posts = Post.objects.all().order_by('-updated')[:20]
        else:
            posts = Post.objects.filter(
                category__slug=category).order_by('-updated')[:20]
    else:
        posts = Post.objects.filter(category=None).order_by('-updated')[:20]

    data = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context=data,)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context=data)


def post_create_view(request, category=None):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(resolve_url('post_detail', post.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'post/post_create.html', {'form': form})
