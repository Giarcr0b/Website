# Generated by Django 3.1.5 on 2021-07-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210616_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type_of_service',
            field=models.CharField(choices=[('IT Support and Mentoring', 'IT Support and Mentoring'), ('PC / Laptop Maintenance and Upgrades', 'PC / Laptop Maintenance and Upgrades'), ('Tuition', 'Tuition'), ('Website Maintenance and Admin', 'Website Maintenance and Admin'), ('Web Development', 'Web Development'), ('CMS Based Web Development', 'CMS Based Web Development'), ('Mobile App Development', 'Mobile App Development')], max_length=80),
        ),
    ]