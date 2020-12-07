from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Pet, Playdate, Review
from .forms import *
from django.urls import reverse

# Create your views here.
class ShowOwnerPageView(DetailView):
    '''shows an owner's profile page'''

    model = Owner
    template_name = "project/show_owner_page.html"
    context_object_name = "owner"

class ShowPetPageView(DetailView):
    '''shows a pet's profile page'''

    model = Pet
    template_name = "project/show_pet_page.html"
    context_object_name = "pet"

class ShowPlaydateView(DetailView):
    '''shows a playdate's details'''

    model = Playdate
    template_name = "project/show_playdate_page.html"
    context_object_name = "playdate"

class ShowReviewView(DetailView):
    '''shows a review of a playdate'''

    model = Review
    template_name = "project/show_playdate_review.html"
    context_object_name = "review"

class ShowAllPetsView(ListView):
    '''shows all pets'''

    model = Pet
    template_name = "project/show_all_pets.html"
    context_object_name = "pets"

class ShowAllPlaydatesView(ListView):
    '''shows all playdates'''

    model = Playdate
    template_name = "project/show_all_playdates.html"
    context_object_name = "playdates"

    # get context data
    def get_context_data(self, **kwargs):
        '''return context data for playdates view'''

        context = super(ShowAllPlaydatesView, self).get_context_data(**kwargs)
        pet_pk = self.kwargs['pk']
        pd = Playdate.objects.filter(pet=pet_pk)
        context['playdates'] = pd
        pet_pk = self.kwargs['pk']
        context['pk'] = pet_pk
        return context


class CreateOwnerProfileView(CreateView):
    '''shows the create owner profile form'''

    model = Owner
    form_class = CreateOwnerProfileForm
    template_name = "project/create_owner_form.html"

class CreatePetProfileView(CreateView):
    '''shows the create pet profile form'''

    model = Pet
    form_class = CreatePetProfileForm
    template_name = "project/create_pet_form.html"

class CreatePlaydateView(CreateView):
    '''shows the create playdate form'''

    model = Playdate
    form_class = CreatePlaydateForm
    template_name = "project/create_playdate_form.html"



    