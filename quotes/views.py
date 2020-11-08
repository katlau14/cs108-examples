from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Quote, Person
from django.urls import reverse
from django.shortcuts import redirect
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
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
        quotes = Quote.objects.all()
        #select one at random
        q = random.choice(quotes)
        return q

class PersonPageView(DetailView):
    '''Display a single person object'''
    model = Person
    template_name = "quotes/person.html"
    #context_object_name = "person"

    def get_context_data(self, **kwargs):
        '''return a dictionary with context data for this template to use'''

        context = super(PersonPageView, self).get_context_data(**kwargs)

        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        return context

class CreateQuoteView(CreateView):
    '''create a new Quote object and store it in the database'''

    model = Quote
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote_form.html"

class UpdateQuoteView(UpdateView):
    '''update a new Quote object and store it in the database'''

    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote_form.html"
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    '''update a new Quote object and store it in the database'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    #success_url = "../../all"

    def get_success_url(self):
        '''return a URL to which we should be directed after the delete'''

        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()

        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})

def add_image(request, pk):
    '''a custom view function to handle the submission of an image upload'''

    person = Person.objects.get(pk=pk)
    form = AddImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        image = form.save(commit=False)
        image.person = person
        image.save()

    else:
        print("Error: the form was not valid.")

    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)