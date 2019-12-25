from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for item in context:
            print(item, ": ", context[item])
        return context

class ArtistListView(generic.ListView):
    model = Artist
    template_name = 'artist_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for item in context:
            print(item, ": ", context[item])
        return context

class ArtistCreate(generic.CreateView):
    model = Artist
    template_name = 'artist_add.html'
    success_url = reverse_lazy('artist_list')
    fields = '__all__'


class ArtistUpdate(generic.UpdateView):
    model = Artist
    template_name = 'artist_update.html'
    success_url = reverse_lazy('artist_list')
    fields = '__all__'

class ArtistDelete(generic.DeleteView):
    model = Artist
    template_name = 'artist_delete.html'
    success_url = reverse_lazy('artist_list')

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'album_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AlbumListView(generic.ListView):
    model = Album
    template_name = 'album_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class AlbumCreate(generic.CreateView):
#     model = Album
#     template_name = 'album_add.html'
#     success_url = reverse_lazy('album_list')
#     fields = '__all__'

# class AlbumUpdate(generic.UpdateView):
#     model = Album
#     template_name = 'album_update.html'
#     success_url = reverse_lazy('album_list')
#     fields = '__all__'

# class AlbumDelete(generic.DeleteView):
#     model = Album
#     template_name = 'album_delete.html'
#     success_url = reverse_lazy('album_list')

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            return redirect(to='album_list')
    else:
        form = AlbumForm()

    return render(request, 'album_add.html', {'form':form})

