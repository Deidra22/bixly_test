# Generated by Django 3.0.7 on 2020-06-21 07:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trucks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vin', models.CharField(default=None, max_length=17)),
                ('current_mileage', models.IntegerField(null=True)),
                ('year', models.IntegerField(default=None)),
                ('make', models.CharField(choices=[('CHEVROLET', 'Chevrolet'), ('DODGE', 'Dodge'), ('FORD', 'Ford'), ('HONDA', 'Honda')], default='Chevrolet', max_length=20)),
                ('model', models.CharField(choices=[('Chevrolet', (('Avalanche', 'Avalanche'), ('Colorado', 'Colorado'), ('Silverado', 'Silverado'))), ('Dodge', (('Dakota', 'Dakota'), ('Ram 1500', 'Ram 1500'), ('Ram 2500', 'Ram 2500'))), ('Ford', (('F150', 'F150'), ('F250', 'F250'), ('F350', 'F350'))), ('Honda', (('Ridgeline Sport', 'Ridgeline Sport'), ('Ridgeline RTL', 'Ridgeline RTL'), ('Ridgeline Black', 'Ridgeline Black')))], default=None, max_length=20)),
                ('seats', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='2', max_length=20)),
                ('bed_length', models.CharField(choices=[('5ft', '5ft'), ('5.5ft', '5.5ft'), ('6ft', '6ft'), ('6.5ft', '6.5ft'), ('7ft', '7ft'), ('7.5ft', '7.5ft'), ('8ft', '8ft')], default='5ft', max_length=6)),
                ('color', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('BLACK', 'Black'), ('SILVER', 'Silver'), ('WHITE', 'White'), ('GOLD', 'Gold')], default=None, max_length=6)),
                ('service_interval', models.CharField(choices=[('3 Months', '3 Months'), ('6 Months', '6 Months'), ('9 Months', '9 Months'), ('12 Months', '12 Months')], default='3 Months', max_length=12)),
                ('next_service', models.DateField(verbose_name='Next Service Date')),
            ],
            options={
                'verbose_name_plural': 'Trucks',
            },
        ),
    ]
