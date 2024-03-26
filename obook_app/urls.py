from django.urls import path
from .views import (
    LandingPageView,
    AboutPageView,
    FaqPageView,
    ContactPageView,
    BookDetailPageView,
    BookListPageView,
)

urlpatterns = [
    path("", LandingPageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("faq/", FaqPageView.as_view(), name="faq"),
    path("occurences/", BookListPageView.as_view(), name="occurences"),
    path("occurence/<int:pk>/", BookDetailPageView.as_view(), name="occurence_detail"),
]
