# Generated by Django 3.1.7 on 2021-03-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20210305_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]