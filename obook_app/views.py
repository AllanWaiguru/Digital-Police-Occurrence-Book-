from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'obook_app/homepage.html'