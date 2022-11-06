from django.shortcuts import render, redirect, get_object_or_404
from .models import post
from django.views import generic, View
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm, Commentform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Views for post list


class postslist(generic.ListView):
    model = post
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 9


# view for individual post

class postdetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = post.objects.filter(status=1)
        posting = get_object_or_404(queryset, slug=slug)
        comments = posting.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if posting.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post.html",
            {
                "post": posting,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": Commentform()
            },
        )
    
    def posting(self, request, slug, *args, **kwargs):

        queryset = post.objects.filter(status=1)
        posting = get_object_or_404(queryset, slug=slug)
        comments = posting.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if posting.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)
