# Generated by Django 2.0 on 2018-06-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_auto_20180308_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catlog',
            name='category',
            field=models.SlugField(max_length=200),
        ),
    ]
