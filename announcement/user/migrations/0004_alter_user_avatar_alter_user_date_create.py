# Generated by Django 4.0.1 on 2022-01-15 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_avatar_alter_user_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]