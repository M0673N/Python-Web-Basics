# Generated by Django 4.0.2 on 2022-02-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='media/images/user.png', upload_to='images'),
        ),
    ]
