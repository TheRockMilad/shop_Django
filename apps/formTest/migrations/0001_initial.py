# Generated by Django 4.2.2 on 2023-07-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200, verbose_name="عنوان پست ")),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="توضیحات"),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]