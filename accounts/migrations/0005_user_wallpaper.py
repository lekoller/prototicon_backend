# Generated by Django 3.1.7 on 2021-03-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210306_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallpaper',
            field=models.ImageField(blank=True, null=True, upload_to='wallpapers/'),
        ),
    ]
