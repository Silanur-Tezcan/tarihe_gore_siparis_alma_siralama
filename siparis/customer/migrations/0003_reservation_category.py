# Generated by Django 5.1.6 on 2025-04-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_reservation_date_alter_reservation_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
    ]
