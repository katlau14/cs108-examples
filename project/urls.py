# project/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('all_pets', ShowAllPetsView.as_view(), name="show_all_pets"),
    path('owner/<int:pk>', ShowOwnerPageView.as_view(), name="show_owner_page"),
    path('pet/<int:pk>', ShowPetPageView.as_view(), name="show_pet_page"),
    path('playdate/<int:pk>', ShowPlaydateView.as_view(), name="show_playdate_page"),
    path('review/<int:pk>', ShowReviewView.as_view(), name="show_playdate_review"),
    path('create_owner_profile', CreateOwnerProfileView.as_view(), name="create_owner_form"),
    path('create_pet_profile', CreatePetProfileView.as_view(), name="create_pet_form"),
    path('create_playdate', CreatePlaydateView.as_view(), name="create_playdate_form"),
    path('all_playdates/<int:pk>', ShowAllPlaydatesView.as_view(), name="show_all_playdates"),
    path('create_review', CreateReviewView.as_view(), name="create_review_form"),
    path('playdate/<int:playdate_pk>/delete_review/<int:review_pk>', DeleteReviewView.as_view(), name = "delete_review"),
    path('owner/<int:pk>/update', UpdateOwnerView.as_view(), name = "update_owner_form"),
    path('pet/<int:pk>/update', UpdatePetView.as_view(), name="update_pet_form"),
    


]