from django.db import models
from django.urls import reverse
import random

# Create your models here.
class Person(models.Model):
    '''represent a Person who said something notable'''
    name = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of this person'''
        return self.name

    def get_random_image(self):
        '''return an image of this person selected at random'''

        images = Image.objects.filter(person=self)
        return random.choice(images)

    def get_all_quotes(self):
        '''return all quotes for this person'''

        return Quote.objects.filter(person=self)

    def get_all_images(self):
        '''return all images for this person'''

        return Image.objects.filter(person=self)

class Quote(models.Model):
    '''Represents a quote by a famous person.'''

    text = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    #author = models.TextField(blank=True)
    #image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a string representation of this quote'''

        return f'"{self.text}" - {self.person}'

    def get_absolute_url(self):
        '''provide a url to show this object'''

        #'quote/<int:pk>'
        return reverse('quote', kwargs={'pk':self.pk})

class Image(models.Model):
    '''represent an image URL for a person'''

    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        '''return the image url of this image'''

        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url