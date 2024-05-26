from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse


# Create your views here.

def fun0(request):
    context = {
        'name': 'mehdi',
    }
    return render(request, 'viewtest/page0.html', context)


# --------------------------------------------------------------
class ViewClass1(View):
    def get(self, request):
        context = {
            'name': 'ali',
        }
        return render(request, 'viewtest/setsession.html', context)


# --------------------------------------------------------------
# عمل ساخت
class PostCreate(CreateView):
    model = Post
    fields = '__all__'

    # success_url="/viewtest/list"

    def get_success_url(self):
        return reverse('ShowList')


# --------------------------------------------------------------
# عمل درج 
class PostList(ListView):
    model = Post
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().order_by('-id')




# --------------------------------------------------------------
class PostDetail(DetailView):
    model = Post


# --------------------------------------------------------------
class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/viewtest/list'


# --------------------------------------------------------------
class PostDelete(DeleteView):
    model = Post
    fields = '__all__'
    success_url = '/viewtest/list'


# --------------------------------------------------------------
class GenericClass1(ListView):
    model = Post
    template_name = "viewtest/getsession.html"
    context_object_name = 'Posts'
    queryset = Post.objects.order_by('is_active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "milad"
        return context


# --------------------------------------------------------------
class GenericClass3(ListView):
    model = Post
    template_name = "viewtest/page3.html"
    context_object_name = 'Posts'
    paginate_by = 6


# --------------------------------------------------------------
from django.core.paginator import Paginator


def fun1(request):
    posts = Post.objects.order_by("is_active")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_obj': page_object
    }
    return render(request, 'viewtest/page4.html', context)


# --------------------------------------------------------------
class GenericClass5(ListView):
    model = Post
    template_name = "viewtest/page5.html"
    context_object_name = 'Posts'

    def get_queryset(self):
        title1 = self.request.GET.get("title")
        new_context = Post.objects.filter(title=title1)
        return new_context
