# Generated by Django 3.0.3 on 2020-04-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_remove_book_auther'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='auther_name',
            field=models.CharField(max_length=36, null=True),
        ),
    ]