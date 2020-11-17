from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Pet, Playdate, Review

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