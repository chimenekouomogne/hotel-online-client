# Generated by Django 2.2.3 on 2019-08-12 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]
