# Generated by Django 3.1.5 on 2021-02-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210128_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type_of_service',
            field=models.CharField(choices=[('IT Support and Mentoring', 'IT Support and Mentoring'), ('Tuition', 'Tuition'), ('Cloud Based Web Development', 'Cloud Based Web Development'), ('Web Development', 'Web Development'), ('Hardware Maintenance and Upgrades', 'Hardware Maintenance and Upgrades'), ('Software Maintenance and Admin', 'Software Maintenance and Admin'), ('Mobile App Development', 'Mobile App Development')], max_length=80),
        ),
    ]
