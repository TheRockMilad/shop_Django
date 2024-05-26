from django.db import models

# Create your models here.

class blog2(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    descrioption =  models.TextField(verbose_name="متن مقاله")
    is_active = models.BooleanField(default=False, verbose_name="وضعیت فعال/غیرفعال")
    main_img = models.ImageField(upload_to='images/blogimg',verbose_name="تصویر اصلی مقاله")
    
    def __str__(self) -> str:
        return self.title+"\n"+self.descripiton+'\n'+str(self.is_active)