# Generated by Django 4.1.6 on 2023-02-06 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GoodsCategory",
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
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sobun",
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
                ("time", models.DateTimeField()),
                ("whether", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Sobun",
            },
        ),
        migrations.CreateModel(
            name="SobunPost",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("picture", models.ImageField(upload_to="pictures/post")),
                ("is_deleted", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("product", models.CharField(max_length=100)),
                ("place", models.CharField(max_length=100)),
                ("schedule", models.DateTimeField()),
                ("sobun_price", models.IntegerField()),
                ("sobun_unit", models.CharField(max_length=30)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SobunTag",
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
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SobunRate",
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
                ("type", models.IntegerField()),
                ("detail", models.TextField(max_length=300)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "sobun",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.sobun",
                    ),
                ),
            ],
        ),
    ]
