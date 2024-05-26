from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'sessiontest/index.html')

def set_session(request):
    request.session['email'] = 'aaaaa@gmail.com'
    request.session['password'] = 'eeeee'
    return render(request,'sessiontest/setsession.html')

def get_session(request):
    email = request.session['email']
    password = request.session['password']
    context = {
        'email': email,
        'password' : password
    }
    return render(request,'sessiontest/getsession.html',context)

def delete_session(request):
    flag = False
    if 'email' in request.session:
        del request.session['email']
        del request.session['password']
        flag = True
    return render(request,'sessiontest/deleteSession.html',{'flag' : flag})