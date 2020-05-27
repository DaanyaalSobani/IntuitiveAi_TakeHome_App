# Generated by Django 3.0.6 on 2020-05-27 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_portal', '0005_auto_20200527_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_request_JSON', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_portal.Organization')),
                ('wastemanager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_portal.WasteManager')),
            ],
        ),
    ]