# Generated by Django 4.1.6 on 2023-02-06 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sobunrate",
            name="user_from",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ratings_given",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="sobunrate",
            name="user_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ratings_received",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="sobunpost",
            name="area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.area",
            ),
        ),
        migrations.AddField(
            model_name="sobunpost",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.goodscategory",
            ),
        ),
        migrations.AddField(
            model_name="sobunpost",
            name="tags",
            field=models.ManyToManyField(to="app.sobuntag"),
        ),
        migrations.AddField(
            model_name="sobunpost",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sobun_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="sobun",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.sobunpost",
            ),
        ),
        migrations.AddField(
            model_name="sobun",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sobuns",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="sobun",
            unique_together={("post", "user")},
        ),
        migrations.AlterIndexTogether(
            name="sobun",
            index_together={("post", "user")},
        ),
    ]
