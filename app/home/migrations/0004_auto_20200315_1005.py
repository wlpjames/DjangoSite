# Generated by Django 3.0.4 on 2020-03-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200314_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_slider',
            name='image',
            field=models.ImageField(upload_to='projects/static/img/'),
        ),
    ]
