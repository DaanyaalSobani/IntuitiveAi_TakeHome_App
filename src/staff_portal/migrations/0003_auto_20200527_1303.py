# Generated by Django 3.0.6 on 2020-05-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_portal', '0002_auto_20200527_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changerequest',
            name='closed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]