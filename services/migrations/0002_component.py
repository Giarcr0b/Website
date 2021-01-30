# Generated by Django 3.1.5 on 2021-01-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('services', models.ManyToManyField(to='services.Service')),
            ],
        ),
    ]
