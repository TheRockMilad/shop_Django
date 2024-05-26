from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان پست")
    caption = models.TextField(verbose_name="کپشن پست")
    is_active = models.BooleanField(default=False,verbose_name="وضعیت پست")

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=40,verbose_name="نام")
    email = models.EmailField(max_length=100,verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.name+"/n"+self.message

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس ها با ما'
