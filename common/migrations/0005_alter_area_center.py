# Generated by Django 4.1.6 on 2023-02-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_remove_profile_content_profile_bio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="area",
            name="center",
            field=models.TextField(blank=True),
        ),
    ]
