# Generated by Django 4.2.2 on 2023-07-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("viewtest", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "پست", "verbose_name_plural": "پست ها"},
        ),
        migrations.AlterField(
            model_name="post",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="وضعیت"),
        ),
    ]