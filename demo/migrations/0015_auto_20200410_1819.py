# Generated by Django 3.0.3 on 2020-04-10 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_auto_20200410_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
