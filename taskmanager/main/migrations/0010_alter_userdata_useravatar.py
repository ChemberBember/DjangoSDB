# Generated by Django 4.2.5 on 2023-09-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_userf_projects_usernick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='UserAvatar',
            field=models.ImageField(default='./templates/main/DBimages/userunknow.jpg', null=True, upload_to='./templates/main/DBimages'),
        ),
    ]
