# project/forms.py

from django import forms
from .models import *

class CreateOwnerProfileForm(forms.ModelForm):
    '''a form to create new owner profiles'''

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email = forms.CharField(label="Email", required=True)
    phone = forms.CharField(label="Phone Number", required=True)
    city = forms.CharField(label="City", required=True)

    class Meta:

        model = Owner
        fields = ['first_name', 'last_name', 'email', 'phone', 'city']

class CreatePetProfileForm(forms.ModelForm):
    '''a form to create new owner profiles'''

    name = forms.CharField(label="Name", required=True)
    breed = forms.CharField(label="Breed", required=True)
    age = forms.CharField(label="Age", required=True)
    image = forms.ImageField(label="Image", required=True)
    blurb = forms.CharField(label="About Me", required=True)

    class Meta:

        model = Pet
        fields = ['name', 'breed', 'age', 'image', 'blurb']

class CreatePlaydateForm(forms.ModelForm):
    '''a form to create a new playdate'''

    class Meta:

        model = Playdate
        fields = ['location', 'time', 'owner', 'pet']
