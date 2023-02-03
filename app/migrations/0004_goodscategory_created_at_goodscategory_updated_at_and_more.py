# Generated by Django 4.1.6 on 2023-02-03 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_sobunpost_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="goodscategory",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goodscategory",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="sobuntag",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sobuntag",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
