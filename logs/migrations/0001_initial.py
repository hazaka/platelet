# Generated by Django 2.0.7 on 2018-07-09 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import logs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=10)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to=logs.models.image_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.ManyToManyField(to='utils.Name')),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start', models.PositiveSmallIntegerField(null=True)),
                ('end', models.PositiveSmallIntegerField(null=True)),
                ('etc', models.CharField(max_length=100, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watches', to=settings.AUTH_USER_MODEL)),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watches', to='logs.Piece')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='watch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='logs.Watch'),
        ),
    ]
