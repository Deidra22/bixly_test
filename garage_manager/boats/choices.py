from django.db import models

# Choices.py for Boats models

class BoatMakeChoices(models.Model):
    MAKE_CHOICES = [
        ('CAYMAS BOATS', 'Caymas Boats'),
        ('NORTHWEST BOATS', 'Northwest Boats'),
        ('GRIZZLY', 'Grizzly')
    ]

class BoatModelChoices(models.Model):
    MODEL_CHOICES = [
        ('Caymas Boats', (
                ('26HB','26HB'),
                ('CX 18 C','CX 18 S'),
                ('CX 20','CX 20'),
            )
        ),
        ('Northwest Boats', (
                ('22 SIGNATURE','22 Signature'),
                ('206 FREEDOM','206 Freedom'),
                ('218 NORTHSTAR','218 Northstar'),
            )
        ),
        ('Grizzly', (
                ('1448 JON','1448 Jon'),
                ('1648 JON','1648 Jon'),
                ('1754 JON','1754 Jon'),
            )
        )
    ]

class BoatLengthChoices(models.Model):
    LENGTH_CHOICES = [
        ('14FT', '14ft'),
        ('16FT', '16ft'),
        ('18FT', '18ft'),
        ('20FT', '20ft'),
        ('25FT', '25ft'),
        ('30FT', '30ft')
    ]

class BoatWidthChoices(models.Model):
    WIDTH_CHOICES = [
        ('60IN', '60in'),
        ('70IN', '70in'),
        ('80IN', '80in'),
        ('90IN', '90IN')
    ]

class BoatServiceInterval(models.Model):
    SERVICE_INTERVAL = [
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('18 Months', '18 Months'),
        ('24 Months', '24 Months'),
    ]