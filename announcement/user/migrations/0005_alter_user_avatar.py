# Generated by Django 4.0.1 on 2022-01-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_avatar_alter_user_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/user/'),
        ),
    ]
