# Generated by Django 4.1.9 on 2023-06-23 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_alter_song_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='user',
        ),
    ]
