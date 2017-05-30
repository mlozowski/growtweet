
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm


class Main(FormView):
    template_name = "growtweet/main.html"
    form_class = AuthenticationForm
