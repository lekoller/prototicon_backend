# Generated by Django 3.1.7 on 2021-03-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_auto_20210304_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='contents/media/'),
        ),
    ]
