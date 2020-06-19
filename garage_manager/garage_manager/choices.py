from django.db import models


class carTruckMakeModelChoices(models.Model):
    MAKE = [
        ('ACURA', 'Acura'),
        ('BMW', 'BMW'),
        ('CHEVROLET', 'Chevrolet'),
        ('DODGE', 'Dodge'),
        ('FORD', 'Ford'),
        ('GMC', 'GMC'),
        ('HONDA', 'Honda')
    ]

class carTruckSeatChoices(models.IntegerChoices):
    twoSeater = 2
    threeSeater = 3
    fourSeater = 4
    sixSeater = 6
    sevenSeater = 7