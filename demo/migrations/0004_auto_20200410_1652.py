# Generated by Django 3.0.3 on 2020-04-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200410_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='auther',
        ),
        migrations.AddField(
            model_name='book',
            name='autherName',
            field=models.CharField(default=None, max_length=36),
        ),
    ]
