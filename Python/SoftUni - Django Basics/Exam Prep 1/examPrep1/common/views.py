from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from examPrep1.utils import get_user_obj
from albums.models import Album
from profiles.forms import ProfileCreateForm


class HomePage(ListView, BaseFormView):
    model = Album
    context_object_name = 'albums'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj()
        if profile:
            return ['profiles/home-with-profile.html',]

        return ['profiles/home-no-profile.html',]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
