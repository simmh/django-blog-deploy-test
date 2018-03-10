from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from treebeard.mp_tree import MP_Node
from taggit.managers import TaggableManager

from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.


class Category(MP_Node):
    STATUS_CHOICES = Choices('public', 'private')
    status = StatusField(choices_name='STATUS_CHOICES')
    name = models.CharField(max_length=80)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True,
                               on_delete=models.CASCADE)
    sib_order = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    node_order_by = ['name']

    def __str__(self):
        return "%s %s" % (self.id, self.name)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = Choices('draft', 'published')
    status = StatusField(choices_name='STATUS_CHOICES')
    category = models.ForeignKey(
        Category, blank=True, null=True,  on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return "%s %s - %s - %s" % (self.id, self.category, self.title, self.body[:30])

    def save(self, *args, **kwargs):
        if not self.title:
           self.title = self.body[:20]
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
