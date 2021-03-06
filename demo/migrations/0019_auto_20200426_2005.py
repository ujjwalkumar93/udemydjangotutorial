# Generated by Django 2.2.3 on 2020-04-26 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0018_charecter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charecter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char', to='demo.Book'),
        ),
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surnamename', models.CharField(max_length=20)),
                ('book', models.ManyToManyField(to='demo.Book')),
            ],
        ),
    ]
