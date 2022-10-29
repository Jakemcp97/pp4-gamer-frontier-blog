from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin
from .forms import PostForm


# Register your models here.
@admin.register(post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['author']

    form = PostForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
