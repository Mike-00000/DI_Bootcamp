# Generated by Django 4.2.1 on 2023-06-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]