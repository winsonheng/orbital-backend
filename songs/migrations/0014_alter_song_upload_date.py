# Generated by Django 4.1.9 on 2023-06-27 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0013_alter_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 27, 17, 19, 16, 109446, tzinfo=datetime.timezone.utc)),
        ),
    ]
