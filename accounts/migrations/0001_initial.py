# Generated by Django 3.1 on 2020-08-25 10:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('slug', models.SlugField()),
                ('headline', models.CharField(blank=True, max_length=150)),
                ('bio', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='profile_img')),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]