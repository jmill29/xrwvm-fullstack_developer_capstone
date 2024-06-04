# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    hq_state = models.CharField(max_length = 20)
    hq_city = models.CharField(max_length = 20)

    def __str__(self):
        return '{maker} (located in {city}, {state}): {description}'.format(
            maker = self.name, 
            city = self.hq_city, 
            state = self.hq_state,
            description = self.description
        )

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length = 30)
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    car_type = models.CharField(choices = CAR_TYPES, default = SEDAN,
                                max_length = 20)
    release_year = models.DateField()
    mileage = models.IntegerField()

    def __str__(self):
        return '{make} {model} is a {car_type} with a gas mileage of {mileage} miles/gallon.' \
          .format(
            make = self.make.name,
            model = self.name,
            car_type = self.car_type,
            mileage = self.mileage
          )