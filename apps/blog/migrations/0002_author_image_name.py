# Generated by Django 4.2.2 on 2023-07-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="image_name",
            field=models.CharField(default="nophoto.png", max_length=200),
            preserve_default=False,
        ),
    ]
