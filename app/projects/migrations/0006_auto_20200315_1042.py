# Generated by Django 3.0.4 on 2020-03-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200315_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
