# Generated by Django 4.1.6 on 2023-02-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_alter_locationverification_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trustlevel",
            name="level",
            field=models.FloatField(default=50),
        ),
    ]
