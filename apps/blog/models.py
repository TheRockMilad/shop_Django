from django.utils import timezone
from django.db import models


# Create your models here.
class chiefEditor(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    family = models.CharField(max_length=50, verbose_name="نام خانوادگی")

    def __str__(self):
        return f"{self.name}\t{self.family}"

    class Meta:
        verbose_name = 'سر دبیر'
        verbose_name_plural = 'سر دبیرها'


class Publication(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام انتشارات")
    chiefEditor = models.OneToOneField(chiefEditor, on_delete=models.CASCADE, primary_key=True, verbose_name="سردبیر")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'نشریه'
        verbose_name_plural = 'انتشارات'


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام")
    family = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    nickname = models.CharField(max_length=100, default="without nickname", blank=True, verbose_name="لقب ")
    age = models.IntegerField(default=20, verbose_name="سن")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت')
    Email = models.EmailField(max_length=30, verbose_name="ایمیل")
    url = models.URLField(max_length=200)
    image_name = models.CharField(max_length=200, default="nophoto.png", verbose_name="تصویر")

    def __str__(self):
        return f"({self.name}\t{self.family}\t{self.age}\t{self.Email}\t" \
               f"{self.register_date})"

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name="سن بالای 18 سال")
        ]

 
class Article(models.Model):
    article_title = models.CharField(max_length=300, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100)
    article_text = models.TextField(verbose_name="متن اصلی")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    ARTICLE_STATUS = [
        ('Draft', "پیش نویس"),
        ('publish', "منتشرشده")
    ]
    status = models.CharField(max_length=40, choices=ARTICLE_STATUS, default='Draft', verbose_name="وضعیت مقاله")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name="نویسنده")
    publication = models.ManyToManyField(Publication, verbose_name="انتشارات/سردبیر")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        db_table = "T_Articles"
        ordering = ["article_title", "is_active"]
