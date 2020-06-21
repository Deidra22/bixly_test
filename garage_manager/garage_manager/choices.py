from django.db import models

# Choices.py for Car and Truck apps

# Car and Truck make choices
class CarTruckMakeChoices(models.Model):
    MAKE_CHOICES = [
        ('CHEVROLET', 'Chevrolet'),
        ('DODGE', 'Dodge'),
        ('FORD', 'Ford'),
        ('HONDA', 'Honda')
    ]

# Car model choices ONLY
class CarModelChoices(models.Model):
    CAR_MODELS = [
        ('Chevrolet', (
                ('Aveo','Aveo'),
                ('Impala','Impala'),
                ('Malibu','Malibu'),
            )
        ),
        ('Dodge', (
                ('Avenger','Avenger'),
                ('Challenger','Challenger'),
                ('Dart','Dart'),
            )
        ),
        ('Ford', (
                ('C-Max','C-Max'),
                ('Escape','Escape'),
                ('Mustang','Mustang'),
            )
        ),
        ('Honda', (
                ('Accord','Accord'),
                ('Fit','Fit'),
                ('Insight','Insight'),
            )
        ),
    ]

# Truck model choices ONLY
class TruckModelChoices(models.Model):
    TRUCK_MODELS = [
        ('Chevrolet', (
                ('Avalanche','Avalanche'),
                ('Colorado','Colorado'),
                ('Silverado','Silverado'),
            )
        ),
        ('Dodge', (
                ('Dakota','Dakota'),
                ('Ram 1500','Ram 1500'),
                ('Ram 2500','Ram 2500'),
            )
        ),
        ('Ford', (
                ('F150','F150'),
                ('F250','F250'),
                ('F350','F350'),
            )
        ),
        ('Honda', (
                ('Ridgeline Sport','Ridgeline Sport'),
                ('Ridgeline RTL','Ridgeline RTL'),
                ('Ridgeline Black','Ridgeline Black'),
            )
        ),
    ]

# Car and Truck number of seats choices
class CarTruckSeatChoices(models.Model):
    SEAT_CHOICES = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7')
    ]
    
# Car and Truck service interval choices    
class CarTruckServiceInterval(models.Model):
    SERVICE_INTERVAL = [
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('9 Months', '9 Months'),
        ('12 Months', '12 Months'),
    ]


# Truck Bed Length Choices
class TruckBedLength(models.Model):
    BED_LENGTH = [
        ('5ft','5ft'),
        ('5.5ft','5.5ft'),
        ('6ft','6ft'),
        ('6.5ft','6.5ft'),
        ('7ft','7ft'),
        ('7.5ft','7.5ft'),
        ('8ft','8ft'),
    ]

# Car and Truck Color Choices
class CarTruckColorChoices(models.Model):
    COLOR_CHOICES = [
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('BLACK', 'Black'),
        ('SILVER', 'Silver'),
        ('WHITE', 'White'),
        ('GOLD', 'Gold')
    ]