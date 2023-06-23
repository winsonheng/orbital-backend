# Generated by Django 4.1.9 on 2023-06-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('songs', '0004_song_song_base64'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_base64',
            field=models.FileField(upload_to='songs'),
        ),
        migrations.AlterField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]