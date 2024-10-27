from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from midExam.utils import get_author_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create-post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'


class PostEditView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    form_class = PostEditForm
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'post_id'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'post_id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
