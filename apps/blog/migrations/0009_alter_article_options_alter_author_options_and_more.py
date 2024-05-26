# Generated by Django 4.2.2 on 2023-07-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_chiefeditor_alter_author_email_alter_author_age_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["article_title", "is_active"],
                "verbose_name": "مقاله",
                "verbose_name_plural": "مقالات",
            },
        ),
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "نویسنده", "verbose_name_plural": "نویسندگان"},
        ),
        migrations.AlterModelOptions(
            name="chiefeditor",
            options={"verbose_name": "سر دبیر", "verbose_name_plural": "سر دبیرها"},
        ),
        migrations.AlterModelOptions(
            name="publication",
            options={"verbose_name": "نشریه", "verbose_name_plural": "انتشارات"},
        ),
        migrations.AlterField(
            model_name="author",
            name="nickname",
            field=models.CharField(
                blank=True,
                default="without nickname",
                max_length=100,
                verbose_name="لقب ",
            ),
        ),
        migrations.AddConstraint(
            model_name="author",
            constraint=models.CheckConstraint(
                check=models.Q(("age__gte", 18)), name="age__gte__18"
            ),
        ),
        migrations.AlterModelTable(
            name="article",
            table="T_Articles",
        ),
    ]