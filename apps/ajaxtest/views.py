from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from apps.ajaxtest.models import Post, Like
from .forms import ContactForm


# Create your views here.

def index(request):
    posts = Post.objects.all
    context = {
        'posts': posts
    }
    return render(request, 'ajaxtest/index.html', context)


def like(request):
    if request.method == "GET":
        post_id = request.GET["post_id"]
        like_post = Post.objects.get(id=post_id)
        likepost = Like(post=like_post)
        likepost.save()
        return HttpResponse('Success')
    return HttpResponse('UnSuccess')


# -------------------------------------------------
def contact_form(request):
    form = ContactForm()
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # your code here
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            name = data['name']
            # name = data.get('name')
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(errors, static=400)
    return render(request, "ajaxtest/contact.html", {'form': form})
