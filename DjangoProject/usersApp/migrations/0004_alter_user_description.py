# Generated by Django 5.0.2 on 2024-03-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0003_user_avatar_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
