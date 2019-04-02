# Generated by Django 2.1.7 on 2019-04-01 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_event_is_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date Sent')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Event', verbose_name='Event Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Chat Messages',
                'verbose_name': 'Chat Message',
            },
        ),
        migrations.RemoveField(
            model_name='chat',
            name='room',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
