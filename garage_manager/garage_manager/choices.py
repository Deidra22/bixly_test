from django.db import models

# Car and Truck make choices
class carTruckMakeChoices(models.Model):
    MAKE_CHOICES = [
        ('ACURA', 'Acura'),
        ('BMW', 'BMW'),
        ('CHEVROLET', 'Chevrolet'),
        ('DODGE', 'Dodge'),
        ('FORD', 'Ford'),
        ('GMC', 'GMC'),
        ('HONDA', 'Honda')
    ]

# Car model choices ONLY
class carModelChoices(models.Model):
    CAR_MODELS = [
        ('Acura', (
                ('ILX','ILX'),
                ('MDX','MDX'),
                ('RDX','RDX'),
            )
        ),
        ('BMW', (
                ('128','128'),
                ('228','228'),
                ('530','530'),
            )
        ),
    ]

# Car and Truck number of seats choices
class carTruckSeatChoices(models.Model):
    SEAT_CHOICES = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7')
    ]
