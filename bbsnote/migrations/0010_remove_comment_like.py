# Generated by Django 4.1.7 on 2023-03-29 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbsnote', '0009_comment_like_alter_comment_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
    ]