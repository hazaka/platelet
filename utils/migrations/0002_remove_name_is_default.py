# Generated by Django 2.0.7 on 2018-07-09 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='is_default',
        ),
    ]