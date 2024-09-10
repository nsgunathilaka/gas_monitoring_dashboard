# Generated by Django 4.1.13 on 2024-06-29

from django.db import migrations


def add_sri_lanka_districts(apps, schema_editor):
    District = apps.get_model('location_management', 'District')
    districts = [
        "Ampara", "Anuradhapura", "Badulla", "Batticaloa", "Colombo", "Galle",
        "Gampaha", "Hambantota", "Jaffna", "Kalutara", "Kandy", "Kegalle",
        "Kilinochchi", "Kurunegala", "Mannar", "Matale", "Matara", "Moneragala",
        "Mullaitivu", "Nuwara Eliya", "Polonnaruwa", "Puttalam", "Ratnapura",
        "Trincomalee", "Vavuniya"
    ]

    for district_name in districts:
        District.objects.create(district=district_name)


class Migration(migrations.Migration):
    dependencies = [
        ('location_management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sri_lanka_districts),
    ]
