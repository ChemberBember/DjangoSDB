# Generated by Django 4.2.5 on 2023-09-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_userdata_useravatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='UserAvatar',
            field=models.ImageField(default='./static/DbImages/DBimages/userunknown.jpg', null=True, upload_to='./static/DbImages/DBimages'),
        ),
    ]
