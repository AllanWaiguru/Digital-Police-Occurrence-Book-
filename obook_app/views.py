from django.views.generic import TemplateView, ListView, DetailView
from .models import Crime


class LandingPageView(TemplateView):
    template_name = "obook_app/homepage.html"


class AboutPageView(TemplateView):
    template_name = "obook_app/about-us.html"


class ContactPageView(TemplateView):
    template_name = "obook_app/contact-us.html"


class FaqPageView(TemplateView):
    template_name = "obook_app/faqs.html"


class BookListPageView(ListView):
    template_name = "obook_app/book-list.html"
    model = Crime
    context_object_name = "occurences"


class BookDetailPageView(DetailView):
    template_name = "obook_app/book-detail.html"
    model = Crime
    context_object_name = "occurence_detail"
