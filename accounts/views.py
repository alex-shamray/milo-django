from django.urls import reverse_lazy
from django.views import generic

from .models import User


class UserListView(generic.ListView):
    model = User
    queryset = User.objects.filter(is_staff=False, is_superuser=False)


class UserDetailView(generic.DetailView):
    model = User


class UserCreateView(generic.CreateView):
    model = User
    fields = ['email']


class UserUpdateView(generic.UpdateView):
    model = User
    fields = ['email']


class UserDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
