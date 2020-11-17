# project/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllPetsView.as_view(), name="show_all_pets"),
    path('owner/<int:pk>', ShowOwnerPageView.as_view(), name="show_owner_page"),
    path('pet/<int:pk>', ShowPetPageView.as_view(), name="show_pet_page"),
    path('playdate/<int:pk>', ShowPlaydateView.as_view(), name="show_playdate_page"),
    path('review/<int:pk>', ShowReviewView.as_view(), name="show_playdate_review"),
    


]