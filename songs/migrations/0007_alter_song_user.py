# Generated by Django 4.1.9 on 2023-06-23 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('songs', '0006_alter_song_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]
