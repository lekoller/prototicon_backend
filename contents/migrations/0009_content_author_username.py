# Generated by Django 3.1.7 on 2021-03-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_auto_20210305_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author_username',
            field=models.CharField(default='Anonymous', max_length=63),
        ),
    ]
