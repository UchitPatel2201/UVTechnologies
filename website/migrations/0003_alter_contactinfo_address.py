# Generated by Django 5.0.2 on 2024-02-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(max_length=30),
        ),
    ]
