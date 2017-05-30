
from django.views.generic import FormView
from django.http import JsonResponse

from growtweet.forms import TwitterUserForm


class Main(FormView):
    template_name = "growtweet/main.html"
    form_class = TwitterUserForm

    def form_valid(self, form):
        return JsonResponse({'status': 'OK'})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
