# Generated by Django 3.0.3 on 2020-04-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20200410_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Books_auther_name',
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
