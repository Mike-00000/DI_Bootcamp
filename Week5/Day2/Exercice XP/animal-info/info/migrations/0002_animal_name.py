# Generated by Django 4.2.1 on 2023-06-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
