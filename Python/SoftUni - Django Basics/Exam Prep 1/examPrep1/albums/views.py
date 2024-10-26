from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from albums.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from albums.models import Album
from examPrep1.utils import get_user_obj


class AddAlbumView(CreateView):
    model = Album
    template_name = 'albums/album-add.html'
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class EditAlbumView(UpdateView):
    model = Album
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    form_class = EditAlbumForm


class DeleteAlbumView(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailsAlbumView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'
