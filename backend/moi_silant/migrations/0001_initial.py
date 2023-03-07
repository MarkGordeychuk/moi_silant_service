# Generated by Django 4.1.7 on 2023-03-07 14:07

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
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory_name', models.CharField(choices=[('MM', 'Machine model'), ('EM', 'Engine model'), ('TM', 'Transmission model'), ('DAM', 'Driving axle model'), ('SAM', 'Steering axle model'), ('MT', 'Maintenance type'), ('FN', 'Failure node'), ('RM', 'Recovery method')], max_length=3)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_number', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('engine_number', models.CharField(max_length=128)),
                ('transmission_number', models.CharField(max_length=128)),
                ('driving_axle_number', models.CharField(max_length=128)),
                ('steering_axle_number', models.CharField(max_length=128)),
                ('supply_contract', models.CharField(max_length=128)),
                ('shipment_date', models.DateField()),
                ('consignee', models.CharField(max_length=128)),
                ('delivery_address', models.CharField(max_length=256)),
                ('complete_set', models.CharField(max_length=256)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('driving_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
                ('machine_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('steering_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('operating_time', models.FloatField()),
                ('work_order_number', models.CharField(max_length=128)),
                ('work_order_date', models.DateField()),
                ('organization', models.CharField(max_length=128)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moi_silant.machine')),
                ('maintenance_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_date', models.DateField()),
                ('operating_time', models.FloatField()),
                ('failure_description', models.TextField()),
                ('spare_parts', models.TextField(blank=True)),
                ('recovery_date', models.DateField(null=True)),
                ('downtime', models.FloatField()),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='moi_silant.machine')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='moi_silant.directory')),
            ],
        ),
    ]