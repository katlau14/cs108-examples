from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    '''model the data attributes of Facebook users'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a string representation of the profile'''

        return f'{self.first_name} {self.last_name}' + '\t' + f'{self.city}' + f'{self.image_url}'
    
    def get_status_messages(self):
        '''obtain messages for profile'''

        return StatusMessage.objects.filter(profile=self)
        

class StatusMessage(models.Model):
    '''model the data attributes of Status message'''
    timestamp = models.DateTimeField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''returns a string representation of the status message'''
        return f"{self.timestamp} {self.message}"