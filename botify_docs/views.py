from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"

class CommunView(TemplateView):
    template_name = "commun.html"
