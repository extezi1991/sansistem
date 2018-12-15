# Generated by Django 2.1.4 on 2018-12-14 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=104),
            preserve_default=False,
        ),
    ]