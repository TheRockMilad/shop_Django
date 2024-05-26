from django.shortcuts import render

# Create your views here.

def index(request):
    context= {

    }
    return render(request,"cookietest/index.html",context)

def set_cookie(request):
    response = render(request,'cookietest/setsession.html')
    response.set_cookie(key='name',value='milad',max_age=2592000)
    response.set_cookie(key='family',value='hosseini',max_age=2592000)
    response.set_cookie(key='age',value='32',max_age=2592000)
    return response

def get_cookie(request):
    context ={}
    if request.COOKIES.get('name'):
        name = request.COOKIES['name']
        family = request.COOKIES['family']
        age = request.COOKIES['age']
        context = {
            'name' : name,
            'family' : family,
            'age': age
        }
    return render(request,'cookietest/getsession.html',context)
