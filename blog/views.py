from django.shortcuts import render
from .models import post
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse

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


def create_post(request):
    template_name = "create_post.html"
    if request.method == 'POST':
        title = request.POST.get('post_title')
        content = request.POST.get('post_content')
        status = 1
        Item.objects.create(title=title, content=content)

        return redirect('home')

    return render(request, 'create_post.html')
