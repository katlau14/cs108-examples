from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    '''model the data attributes of Facebook users'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''return a string representation of the profile'''

        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        '''provide a url to show this object'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})
    
    def get_status_messages(self):
        '''obtain messages for profile'''

        return StatusMessage.objects.filter(profile=self)

    def get_friends(self):
        '''get all friends for this profile'''

        friends = Profile.objects.filter(friends=self)

        return friends

    def get_news_feed(self):
        '''get all status messages by this profile and all its friends'''

        #news = StatusMessage.objects.all().order_by("-timestamp")
        friends = self.get_friends()
        news_pk = [self.pk]
        news_pk += [profile.pk for profile in self.get_friends()]
        news_profile = StatusMessage.objects.filter(profile__in=news_pk)
        return news_profile
        
    def get_friend_suggestions(self):
        '''get friend suggestions for this profile'''

        friends = self.get_friends()
        friends_pk = [self.pk]
        friends_pk += [profile.pk for profile in self.get_friends()]
        possible_friends = friend_suggestions = Profile.objects.exclude(pk__in=friends_pk)
        return possible_friends


class StatusMessage(models.Model):
    '''model the data attributes of Status message'''
    timestamp = models.DateTimeField(default=timezone.now)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''returns a string representation of the status message'''
        return f'{self.timestamp} {self.message}'