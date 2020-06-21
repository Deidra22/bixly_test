# Generated by Django 3.0.7 on 2020-06-20 22:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vin', models.CharField(default=None, max_length=17)),
                ('current_mileage', models.IntegerField(null=True)),
                ('make', models.CharField(choices=[('CHEVROLET', 'Chevrolet'), ('DODGE', 'Dodge'), ('FORD', 'Ford'), ('HONDA', 'Honda')], default='Chevrolet', max_length=20)),
                ('model', models.CharField(choices=[('Chevrolet', (('Aveo', 'Aveo'), ('Impala', 'Impala'), ('Malibu', 'Malibu'))), ('Dodge', (('Avenger', 'Avenger'), ('Challenger', 'Challenger'), ('Dart', 'Dart'))), ('Ford', (('C-Max', 'C-Max'), ('Escape', 'Escape'), ('Mustang', 'Mustang'))), ('Honda', (('Accord', 'Accord'), ('Fit', 'Fit'), ('Insight', 'Insight')))], default=None, max_length=20)),
                ('seats', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='2', max_length=20)),
                ('service_interval', models.CharField(choices=[('3 Months', '3 Months'), ('6 Months', '6 Months'), ('9 Months', '9 Months'), ('12 Months', '12 Months')], default='3 Months', max_length=10)),
                ('next_service', models.DateTimeField(verbose_name='Next Service Date')),
            ],
            options={
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
