from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote, Person
import random
# Create your views here.

class HomePageView(ListView):
    '''show a listing of quotes'''
    model = Quote
    template_name = "quotes/home.html"
    context_object_name = "quotes"

class QuotePageView(DetailView):
    '''Display a single quote object'''
    model = Quote
    template_name = "quotes/quote.html"
    context_object_name = "quote"

class RandomQuotePageView(DetailView):
    '''Display a single quote object'''
    model = Quote
    template_name = "quotes/quote.html"
    context_object_name = "quote" 

    def get_object(self):
        '''select one quote at random'''

        #obtain all quotes using the object manager
        quotes = Quote.object.all()
        #select one at random
        q = random.choice(quotes)
        return q

class PersonPageView(DetailView):
    '''Display a single person object'''
    model = Person
    template_name = "quotes/person.html"
    context_object_name = "person"