from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پست ")
    description = models.TextField(max_length=3000, verbose_name="توضیحات")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " "+self.description

