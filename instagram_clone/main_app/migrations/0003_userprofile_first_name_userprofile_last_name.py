# Generated by Django 4.2 on 2024-05-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_followerscount_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
