from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from .models import Profile, StatusMessage
from django.urls import reverse

# Create your views here.
class ShowAllProfilesView(ListView):
    '''shows all profiles'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"
    
class ShowProfilePageView(DetailView):
    '''shows profile page'''
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''create new profile'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    '''update existing profile'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet
            image = form.save(commit=False)
            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)
            status = StatusMessage.objects.get(pk=pk)
            # attach FK profile to this status message
            status_message.profile = profile
            status_message.save() # now commit to database
        

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class DeleteStatusMessageView(DeleteView):
    '''delete an existing status message'''

    model = Profile
    template_name = "mini_fb/delete_status_form.html"

    def get_context_data(self, **kwargs):
        '''return context data'''

        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['statusmessage'] = st_msg
        profile_pk = self.kwargs['profile_pk']
        context['profile_pk'] = profile_pk
        return context

    def get_object(self):
        '''return status message to be deleted'''

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the Status Message object, and return it
        status = StatusMessage.objects.get(pk=status_pk, profile=profile_pk)
        return status

    def get_success_url(self):
        '''return the URL to which to redirect the user'''

        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        
        return reverse('show_profile_page', kwargs={'pk': profile_pk})

class ShowNewsFeedView(DetailView):
    '''shows news feed of status messages'''

    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile"

class ShowPossibleFriendsView(DetailView):
    '''shows possible friends for a profile'''

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "profile"

def add_friend(request, profile_pk, friend_pk):
    '''add a friend to a given profile'''

    profile = Profile.objects.get(pk=profile_pk)
    friend = Profile.objects.get(pk=friend_pk)
    
    profile.friends.add(friend)
    profile.save()
    return redirect(reverse('show_profile_page', kwargs={'pk': profile_pk}))



