# Generated by Django 3.2.9 on 2022-01-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default/user.png', upload_to='uploads'),
        ),
    ]
