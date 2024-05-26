from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader


# Create your views here.

# def index(request):
#     return render(request,"mainapp/index2.html")


# def step1(request):
#     template = loader.get_template('mainapp/setsession.html')
#     return HttpResponse(template.render())

def index(request):
    context ={
        "media_url":settings.MEDIA_URL,
        "image":"/1.jpg"
    }
    return render(request,'mainapp/index.html',context)
#------------------------------------------------------------
def step2(request):
    context = {
        "name" : "میلاد",
        "age" : 42,
        "n" : 100
    }
    return render(request,'mainapp/getsession.html',context)
#------------------------------------------------------------
def step3(request):
    context = {
        "name" : "میلاد",
        "age" : 42,
        "n" : 100
    }
    return render(request,'mainapp/page3.html',context)
#------------------------------------------------------------
import datetime
def step4(request):
    today = datetime.datetime.now
    context = {
        "name" : "میلاد",
        "age" : 20,
        "n" : 100,
        "today" : today
    }
    return render(request,'mainapp/page4.html',context)
#------------------------------------------------------------
import datetime
def step5(request):
    today = datetime.datetime.now
    context = {
        "name" : "میلاد",
        "age" : 20,
        "n" : 100,
        "today" : today,
        "names" : ["Milad","Hamid","Morteza","Sahba","Maryam","Mohammad"],
        "range" : range(1,21),
        "list1" : ['Milad',"Hamid"],
        "list2" : [],
        
    }
    return render(request,'mainapp/page5.html',context)
#------------------------------------------------------------
def step6(request):
    context = {
        "row" : range(10),
        "col" : range(10)
    }
    return render(request,'mainapp/page6.html',context)
#------------------------------------------------------------
def step7(request):
    context = {
        "mytag" : "<h1 style ='color:green'>میلاد حسینی</h1>",
        "myscript" : "alert('hello')"
    }
    return render(request,'mainapp/page7.html',context)
#------------------------------------------------------------
def step8(request):
    return render(request,'mainapp/page8.html')
#------------------------------------------------------------
def step9(request):
    today = datetime.datetime.now
    list1 = ['hamid','morteza','mohammad','ali']
    context = {
        "str1": "Milad Hosseini",
        "today" : today,
        "list1" : list1
    }
    return render(request,'mainapp/page9.html',context)
#------------------------------------------------------------
def step10(request):
    context = {
        'media_url':settings.MEDIA_URL
    }
    return render(request,'mainapp/page10.html',context)

#------------------------------------------------------------
def step11(request):
    context = {
        'media_url':settings.MEDIA_URL
    }
    return render(request,'mainapp/page11.html',context)
#------------------------------------------------------------
def header(request):
    context = {
        "media_url":settings.MEDIA_URL,
    }
    return render(request,'mainapp/header.html',context)

#------------------------------------------------------------
