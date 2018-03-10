from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Category, Post

# Register your models here.

# class MyAdmin(TreeAdmin):
#     fields = ('title', 'body', 'is_edited',
#               'timestamp', '_position', '_ref_node_id',)
#     form = movenodeform_factory(MyNode)


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, MyAdmin)
admin.site.register(Post)
