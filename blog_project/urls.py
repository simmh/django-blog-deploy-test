"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
] 

urlpatterns += [
    re_path('html/(?P<path>.*)', core_views.serve_html, name='html'),
    # index
    # path('', core_views.index, name='index'),
    path('',
         core_views.post_list_view, {'category': 'all'}, name='post_list'),
    # none category post
    path('category/',
         core_views.post_list_view, name='post_list'), 
    # all or select category
    path('category/<str:category>/',
         core_views.post_list_view, name='post_list'),
    path('post/<int:pk>/', core_views.post_detail_view, name='post_detail'),
    path('post/create/', core_views.post_create_view, name='post_create'),

    # api
    path('api/category/', core_views.get_category_list, name='api_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
