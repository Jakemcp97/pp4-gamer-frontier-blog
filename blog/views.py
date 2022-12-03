from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Post
from django.views import generic, View
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import PostForm, Commentform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView


# Views for post list


class postslist(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 9


# view for individual post

class postdetail(View):
    # get and display post
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": Commentform()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # add comments
        comment_form = Commentform(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = Commentform()

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

# likes method


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# user creation of posts


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)

# edit post


class Editpost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    success_url = reverse_lazy('home')
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)


# delete post
class Deletepost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post.html'

    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(author=self.request.user)
        )
