# Generated by Django 4.0.2 on 2022-02-17 15:02

from django.db import migrations, models
import newExam.profile_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[newExam.profile_app.validators.file_size]),
        ),
    ]
