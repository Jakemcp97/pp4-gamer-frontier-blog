from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
