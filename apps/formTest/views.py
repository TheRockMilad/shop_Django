from django.shortcuts import render, redirect
from django.conf import settings
from .forms import InputForm0, InputForm2, InputForm3, InputForm4, InputForm6, InputForm7
from django.forms import formset_factory
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def formTest(request):
    content = {
        "media_url": settings.MEDIA_URL,
    }
    return render(request, 'formTest/form1.html', content)


def form0(request):
    form = InputForm0()
    context = {
        "media_url": settings.MEDIA_URL,
        'form': form
    }
    return render(request, "formTest/form0.html", context)


def form2(request):
    form = InputForm2()
    context = {
        "media_url": settings.MEDIA_URL,
        'form': form
    }
    return render(request, "formTest/form2.html", context)


def form3(request):
    form = InputForm2()
    context = {
        "media_url": settings.MEDIA_URL,
        'form': form
    }
    return render(request, "formTest/form3.html", context)


def form4(request):
    form = InputForm3()
    context = {
        "media_url": settings.MEDIA_URL,
        'form': form
    }
    return render(request, "formTest/form4.html", context)


def form5(request):
    form = InputForm4()
    context = {
        "media_url": settings.MEDIA_URL,
    }
    if request.method == "POST":
        form = InputForm4(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['name'], data['family'], data['age'], data['is_active'])
        else:
            context['error_message'] = 'اطلاعات فرم معتبر نمی باشد'
    else:
        form = InputForm4()

    context['form'] = form
    return render(request, "formTest/form5.html", context)


def form6(request):
    forms_set = formset_factory(InputForm6, extra=3)
    context = {
        'forms_set': forms_set,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, 'formTest/form6.html', context)


def form7(request):
    context = {}
    form = InputForm7(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        post = Post()
        post.title = data['title']
        post.description = data['description']
        post.is_active = data['is_active']
        post.save()
        # return redirect("index2/")
        return HttpResponseRedirect(reverse('post_index'))
    context = {
        "media_url": settings.MEDIA_URL,
        'form': form
    }
    return render(request, 'formTest/form7.html', context)


def index(request):
    posts = Post.objects.all()
    context={
        "posts" : posts
    }
    return render(request,"formTest/index.html",context)