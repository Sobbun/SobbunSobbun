# Generated by Django 4.1.6 on 2023-02-03 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("chat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatroom",
            name="participants",
            field=models.ManyToManyField(
                related_name="chat_rooms", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="topic_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="chatmessagehistory",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="chat.chatmessage",
            ),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="checked_by",
            field=models.ManyToManyField(
                related_name="checked_messages", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="chat.chatroom",
            ),
        ),
    ]
