from django.db import models

# Create your models here.
class Owner(models.Model):
    '''model the data attributes of the pet owners'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    city = models.TextField(blank=True)
    phone = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of the pet owner'''
        return f'{self.first_name} {self.last_name}'

class Pet(models.Model):
    '''model the data attributes of the pet'''

    name = models.TextField(blank=True)
    breed = models.TextField(blank=True)
    age = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    blurb = models.TextField(blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        '''return a string representation of the pet'''
        return self.name

class Playdate(models.Model):
    '''model the data attributes of a playdate'''

    location = models.TextField(blank=True)
    time = models.DateTimeField(blank=True)
    owner = models.ManyToManyField(Owner, blank=True)
    pet = models.ManyToManyField(Pet, blank=True)

    def __str__(self):
        '''return a string representation of playdate'''
        return f'{self.time}'

    def get_pets(self):
        '''get pets on this playdate'''

        pets = Pet.objects.filter(playdate=self)
        return pets
    
    def get_owners(self):
        '''get owners on this playdate'''

        owners = Owner.objects.filter(playdate=self)
        return owners

class Review(models.Model):
    '''model the data attributes of the playdate review'''

    playdate = models.ForeignKey(Playdate, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        '''return a string representation of the playdate review'''
        return f'{self.timestamp} {self.message}'