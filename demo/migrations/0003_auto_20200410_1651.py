# Generated by Django 3.0.3 on 2020-04-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200410_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='auther',
            field=models.CharField(max_length=36),
        ),
    ]
