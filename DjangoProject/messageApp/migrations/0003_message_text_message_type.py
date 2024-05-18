# Generated by Django 5.0.2 on 2024-05-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageApp', '0002_alter_chatroom_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
