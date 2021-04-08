from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from shortened.models import UrlKeeper


class DetailUrlView(DetailView):
    model = UrlKeeper
    template_name = 'detail.html'


class CreateUrlView(CreateView):
    model = UrlKeeper
    fields = ('original',)
    template_name = 'form.html'



class RedirectToUrl(View):

    def get(self, *args, **kwargs):
        url_keeper = get_object_or_404(UrlKeeper, shortened=kwargs.get("abbreviation"))
        return redirect(url_keeper.original)
