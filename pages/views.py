from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class PicturePageView(TemplateView):
    template_name = 'bgpict.html'