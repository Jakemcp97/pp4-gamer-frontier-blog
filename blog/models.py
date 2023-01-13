from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField
from django import forms
from django.utils.text import slugify

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete")
)


class Post(models.Model):
    # title field
    title = models.CharField(
        max_length=200, unique=True, validators=[MinLengthValidator(10)])
    # Slug field
    slug = models.SlugField(max_length=200, unique=True)
    # author field
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # date and time fields
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    # content field
    content = models.TextField(validators=[MinLengthValidator(10)])
    # content image
    featured_image = CloudinaryField('image', default='placeholder')
    # post status
    status = models.IntegerField(choices=STATUS, default=0)
    # likes on post
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
