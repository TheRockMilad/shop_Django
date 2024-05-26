# Generated by Django 4.2.2 on 2023-07-08 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_rename_id_active_author_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="chiefEditor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="نام")),
                (
                    "family",
                    models.CharField(max_length=50, verbose_name="نام خانوادگی"),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="author",
            name="Email",
            field=models.EmailField(max_length=30, verbose_name="ایمیل"),
        ),
        migrations.AlterField(
            model_name="author",
            name="age",
            field=models.IntegerField(default=20, verbose_name="سن"),
        ),
        migrations.AlterField(
            model_name="author",
            name="family",
            field=models.CharField(max_length=30, verbose_name="نام خانوادگی"),
        ),
        migrations.AlterField(
            model_name="author",
            name="image_name",
            field=models.CharField(
                default="nophoto.png", max_length=200, verbose_name="تصویر"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="فعال/غیرفعال"),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=30, verbose_name="نام"),
        ),
        migrations.AlterField(
            model_name="author",
            name="nickname",
            field=models.CharField(
                blank=True,
                default="without nickname",
                max_length=100,
                verbose_name="لقب",
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="register_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="تاریخ عضویت"
            ),
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="نام انتشارات"),
                ),
                (
                    "chiefEditor",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="blog.chiefeditor",
                        verbose_name="سردبیر",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article_title",
                    models.CharField(max_length=300, verbose_name="عنوان مقاله"),
                ),
                ("slug", models.SlugField(max_length=100)),
                ("article_text", models.TextField(verbose_name="متن اصلی")),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "published_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="تاریخ انتشار"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="فعال/غیرفعال"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Draft", "پیش نویس"), ("publish", "منتشرشده")],
                        default="Draft",
                        max_length=40,
                        verbose_name="وضعیت مقاله",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.author",
                        verbose_name="نویسنده",
                    ),
                ),
                (
                    "publication",
                    models.ManyToManyField(
                        to="blog.publication", verbose_name="انتشارات/سردبیر"
                    ),
                ),
            ],
        ),
    ]