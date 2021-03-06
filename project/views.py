from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Owner, Pet, Playdate, Review
from .forms import *
from django.urls import reverse

# Create your views here.
class HomePageView(TemplateView):
    '''A specialized version of TemplateView to display the home page.'''

    template_name = "project/home.html"

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
    '''shows all pet profiles'''

    model = Pet
    template_name = "project/show_all_pets.html"
    context_object_name = "pets"

class ShowAllPlaydatesView(ListView):
    '''shows all playdates'''

    model = Playdate
    template_name = "project/show_all_playdates.html"
    context_object_name = "playdates"

    def get_context_data(self, **kwargs):
        '''return context data for playdates view'''

        # obtain the default context data (a dictionary) from the superclass
        context = super(ShowAllPlaydatesView, self).get_context_data(**kwargs)
        pet_pk = self.kwargs['pk']
        # filter the playdates for the specific pet
        pd = Playdate.objects.filter(pet=pet_pk)
        # add into context dictionary
        context['playdates'] = pd
        pet_pk = self.kwargs['pk']
        context['pk'] = pet_pk
        # return the context dictionary
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

class CreateReviewView(CreateView):
    '''shows the create review form'''

    model = Review
    form_class = CreateReviewForm
    template_name = "project/create_review_form.html"

class DeleteReviewView(DeleteView):
    '''shows the delete review form'''

    template_name = "project/delete_review_form.html"
    queryset = Playdate.objects.all()

    def get_context_data(self, **kwargs):
        '''return context data for the delete review form'''

        # obtain the default context data (a dictionary) from the superclass
        context = super(DeleteReviewView, self).get_context_data(**kwargs)
        # retrieve the specific review object 
        review = Review.objects.get(pk=self.kwargs['review_pk'])
        context['review'] = review
        #return this context dictionary
        return context

    def get_object(self):
        '''return the review to be deleted'''

        # read the URL data values into variables
        playdate_pk = self.kwargs['playdate_pk']
        review_pk = self.kwargs['review_pk']

        # find the Review object, and return it
        review = Review.objects.get(pk=review_pk)
        return review

    def get_success_url(self):
        '''return the URL to which to redirect the user'''

        playdate_pk = self.kwargs['playdate_pk']
        review_pk = self.kwargs['review_pk']
        
        return reverse('show_playdate_page', kwargs={'pk': playdate_pk})
    
class UpdateOwnerView(UpdateView):
    '''shows the update owner profile form'''

    model = Owner
    form_class = UpdateOwnerForm
    template_name = 'project/update_owner_form.html'

class UpdatePetView(UpdateView):
    '''shows the update pet profile form'''

    model = Pet
    form_class = UpdatePetForm
    template_name = 'project/update_pet_form.html'
