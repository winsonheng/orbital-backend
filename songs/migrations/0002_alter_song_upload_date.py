# Generated by Django 4.1.9 on 2023-05-29 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
