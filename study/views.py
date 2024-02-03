from django.views.generic import TemplateView
from .forms import MeuForm

class Home(TemplateView):
    template_name = "study/home.html"
    form_class = MeuForm