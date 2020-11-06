#forms.py

from django import forms
from django.urls import reverse
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''a form to create new profiles'''

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    image_url = forms.URLField(label="Image URL", required=True)

    class Meta:
        
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email', 'image_url']
        
class UpdateProfileForm(forms.ModelForm):
    '''update an existing profile'''

    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    image_url = forms.URLField(label="Image URL", required=True)

    def get_absolute_url(self):
        '''provide a url to show this object'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})

    class Meta:

        model = Profile
        fields = ['birth_date', 'city', 'email', 'image_url']

class CreateStatusMessageForm(forms.ModelForm):
    '''a form to create a new status message'''

    class Meta:

        model = StatusMessage
        fields = ['timestamp', 'message']