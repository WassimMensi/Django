# Generated by Django 5.1.3 on 2024-12-05 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorites',
        ),
    ]
