from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
