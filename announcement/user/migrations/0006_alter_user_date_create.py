# Generated by Django 4.0.1 on 2022-01-15 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 14, 35, 18, 230782, tzinfo=utc)),
        ),
    ]