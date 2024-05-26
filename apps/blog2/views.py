from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import blog2
from django.core.files.storage import FileSystemStorage
import os
import datetime
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives

# Create your views here.

def index(request):
    blog = blog2.objects.all()
    context = {
        'blogs' : blog,
        'media_url': settings.MEDIA_URL,
    }
    return render(request,'blog2/index.html',context)

#-------------------------------------------------------------

def sendEmail(subject,message,to):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,to)

# این متد دو حالت داره
# یا پست اومده یا گت اومده
# دور اول حتما پست نیست
# و میره توی الس
# دفعه بعدی که کاربر کار رو از سمت اچ تی ام ال انجام میده
def Create_blog(request):
    # عمل پست اتفاق افتاده
    if request.method == "POST":
        # اطلاعات پست شده دریافت میشه 
        form = BlogForm(request.POST,request.FILES)
        # اعتبار سنجی میشه
        if form.is_valid():
            #اطلاعات عکس هم گرفته میشه 
            imageUpload = request.FILES['main_img']
            # اگر کمتر از یک مقدار بود انجام بده  
            if imageUpload.size < 100000 : 
                # اگر نوع فایل این دوتا بود 
                if imageUpload.content_type == "image/jpeg" or imageUpload.content_type == "image/png":
                    imgName,exe = os.path.splitext(imageUpload.name)
                    currenttime = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
 
                    imagePath = 'images/blogimg/'+imgName + currenttime + exe
                    # imagePath = 'images/blogimg/'+imageUpload.name
                    # داده ها برداشته میشه 
                    data = form.cleaned_data
                    # داده ها یک به یک انتخاب میشه و پیدا میشه
                    blog = blog2()
                    blog.title =data['title']
                    blog.descrioption =data['descrioption']
                    blog.is_active =data['is_active']
                    #اینجا میدیمش به سرور
                    blog.main_img = imagePath
                    # در نهایت ذخیره میشه
                    blog.save()
                    # ارسال بشه به یک صفحه دیگه
                    fss = FileSystemStorage()
                    fss.save(imagePath,imageUpload)
                    sendEmail('ذخیره مقاله',
                              'مقاله با موفقیت درج شد ',
                              ['sub.milad1990@gmail.com'],
                              )
                    context = {
                         'form' : form,
                         'message' : 'ثبت شد',
                               }
                    return redirect(request,"blog2/index.html",context)
                # در غیر این صورت 
                else:
                    context ={
                        'form' : form,
                        'message' : "نوع فایل اشتباه است"
                    }
                    return render(request,'blog2/index.html',context) 
            # در غیر اینصورت
            else:
                context ={
                    'form' : form,
                    'message' : 'سایز تصویر نباید بیشتر از 100 کیلوبایت باشد'
                }
                return render(request,'blog2/index.html',context)
        else:
            context ={
                'form' : form,
                'message' : 'فرم نامعتبر است',
                #ارور های برنامه رو هم نشون میده 
                'errors' : form.errors,
            }
            return render(request,'blog2/index.html',context)
    else:
        form = BlogForm()
        context = {
            'form' : form,
        }
        return render(request,'blog2/create.html',context)
# این شد ذخیره‌سازی داده های غیر تصویری
