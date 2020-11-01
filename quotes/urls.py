# quotes/urls.py

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('all', QuotePageView.as_view(), name="all_quotes"),
    path('quote/<int:pk>', QuotePageView.as_view(), name="quote"),
    
]