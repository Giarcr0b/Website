# Generated by Django 3.1.5 on 2021-05-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20210513_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='image_name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
