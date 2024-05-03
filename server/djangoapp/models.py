# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fun_fact = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    CAR_TYPES = [
        ("SALOON", "Saloon"),
        ("SUV", "SUV"),
        ("ESTATE", "Estate"),
        ("HATCHBACK", "Hatchback")
    ]

    car_type = models.CharField(max_length=10, choices=CAR_TYPES,
                                default="SUV")
    year = models.IntegerField(default=2024,
                               validators=[
                                MaxValueValidator(2024),
                                MinValueValidator(1901)
                                ]
                               )

    def __str__(self):
        return self.name
