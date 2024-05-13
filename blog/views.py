from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from blog.forms import PostForm
from .models import Post
from django.views.generic.edit import DeleteView


class SupprimerPost(DeleteView):
    model = Post
    template_name = 'blog/supprimer_post.html'  # Your template for confirmation
    success_url = reverse_lazy('liste_post')


class Listeposts(ListView):
    model = Post
    template_name = 'blog/Liste_post.html'
    context_object_name = 'posts'


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/détail_post.html'
    context_object_name = 'posts'

class CreerPost(CreateView):
    model = Post
    template_name = 'blog/creer_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_post')

class ModifierPost(UpdateView):
    model = Post
    template_name = 'blog/modifier_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_post')
