# Generated by Django 4.1.9 on 2023-06-27 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0014_alter_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 27, 17, 25, 50, 968826, tzinfo=datetime.timezone.utc)),
        ),
    ]
