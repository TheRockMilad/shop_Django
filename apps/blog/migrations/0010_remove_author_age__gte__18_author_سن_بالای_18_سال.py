# Generated by Django 4.2.2 on 2023-07-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_alter_article_options_alter_author_options_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="author",
            name="age__gte__18",
        ),
        migrations.AddConstraint(
            model_name="author",
            constraint=models.CheckConstraint(
                check=models.Q(("age__gte", 18)), name="سن بالای 18 سال"
            ),
        ),
    ]
