from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length = 20)
    model = models.CharField(max_length = 45)
    year = models.IntegerField(null=True, validators=[MinValueValidator(1900),MaxValueValidator(2024)])
    engine = models.CharField(max_length = 25)
    transmission = models.CharField(max_length = 25)
    vin = models.CharField(max_length = 17)
    about_car = models.TextField(default='')
    price_usd = models.IntegerField(null=True, validators=[MinValueValidator(100),MaxValueValidator(1500)])
    slug = models.SlugField(null=False, db_index=True, unique=True)
    status = models.BooleanField(default=False)
    images = models.ImageField(upload_to = 'cars', default='')


    def get_url(self):
        return reverse ('name_site_car',args = [self.slug])

    def __str__(self):
        return f'{self.make} {self.model}'
    


class Feedback(models.Model):
    name = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    feedback = models.TextField(validators=[MinLengthValidator(7)])
    email = models.EmailField(max_length=60)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
class UserClient(models.Model):

    ClienCodPhone = [
        ('+375', '+375'),
        ('80', '80')
    ]

    name = models.CharField(max_length=15,validators=[MinLengthValidator(3)])
    phone = models.CharField(max_length=9,validators=[MinLengthValidator(9)])
    codphone = models.CharField(max_length=4, choices=ClienCodPhone, default='+375')
    ClientChoice = models.CharField(max_length=66, default="Нужна помощь в подборе")
    time = models.DateTimeField(auto_now=True)