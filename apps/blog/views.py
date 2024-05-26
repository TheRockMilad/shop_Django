from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.conf import settings
from .models import Author

# Create your views here.

def index(request):
    authors=Author.objects.all()
    context = {
        "authors" : authors,
        "media_url": settings.MEDIA_URL,
        "imageName": '1.jpg', }
    return render(request,'blog/setsession.html',context)
#---------------------------------------------------
def showAuthors(request):
    authors=Author.objects.all()
    context = {
        "authors" : authors,
        "media_url" : settings.MEDIA_URL
    }
    return render(request,'blog/Authors.html',context)
#---------------------------------------------------
def showAuthorsDetails(request,author_id):
    try:
        authors=Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("صفحه مورد نظر یافت نشد")
    context = {
        "authors" : authors,
        "media_url": settings.MEDIA_URL
    }
    return render(request,'blog/authorDetails.html',context)

