# Generated by Django 4.1.13 on 2024-09-10 08:22

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location_management', '0002_add_sri_lanka_districts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='cites',
            field=djongo.models.fields.JSONField(blank=True, null=True),
        ),
    ]