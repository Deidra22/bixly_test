# Generated by Django 3.0.7 on 2020-06-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='next_service',
            field=models.DateField(verbose_name='Next Service Date'),
        ),
    ]
