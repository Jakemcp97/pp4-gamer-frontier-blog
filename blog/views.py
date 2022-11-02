from django.shortcuts import render, redirect
from .models import post
from django.views import generic, View
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('blog:home')  # validating
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create_post.html', context)


def success(request):
    return HttpResponseRedirect("home.html")
