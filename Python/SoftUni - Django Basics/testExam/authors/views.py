from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author
from midExam.utils import get_author_obj


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'authors/create-author.html'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dashboard')


class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_author_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_updated_post = self.object.posts.order_by('-updated_at').first()
        context['last_updated_post'] = last_updated_post
        return context


class AuthorEditView(UpdateView):
    model = Author
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')
    form_class = AuthorEditForm

    def get_object(self, queryset=None):
        return get_author_obj()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author_obj()
