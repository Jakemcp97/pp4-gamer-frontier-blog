from django.shortcuts import render
from .models import post
from django.views import generic, View
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm

# Views for post list


class postslist(generic.ListView):
    model = post
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4

# view for individual post


class postdetail(generic.DetailView):
    model = post
    template_name = "post.html"


def blog_post(request):

    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Post(
                title=post_form.cleaned_data["title"],
                author=post_form.cleaned_data["author"],
                body=post_form.cleaned_data["body"],
            )
            post.save()

    context = {
        "post_form": post_form,
    }

    args = {}
    args['post_form'] = post_form

    return render(request, "create_post.html", args)
