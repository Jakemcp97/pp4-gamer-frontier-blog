from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms
from django.utils.text import slugify

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete")
)


class post(models.Model):
    # title field
    title = models.CharField(max_length=200, unique=True)
    # Slug field
    slug = models.SlugField(max_length=200, unique=True)
    # author field
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # date and time fields
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    # content field
    content = models.TextField()
    # content image
    featured_image = CloudinaryField('image', default='placeholder')
    # post status
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(post, self).save(*args, **kwargs) 

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
