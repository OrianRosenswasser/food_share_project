# Generated by Django 5.1.3 on 2024-11-13 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_foodpost_whatsapp_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodrequest',
            name='requested_at',
        ),
        migrations.RemoveField(
            model_name='foodrequest',
            name='status',
        ),
        migrations.AddField(
            model_name='foodrequest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='foodrequest',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodrequest',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='foodrequest',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]