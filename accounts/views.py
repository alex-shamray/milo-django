from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import User


class UserListView(generic.ListView):
    model = User
    queryset = User.objects.filter(is_staff=False, is_superuser=False)
    paginate_by = 10


class UserDetailView(generic.DetailView):
    model = User


class UserCreateView(generic.CreateView):
    model = User
    fields = ['email']


class UserUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'users.can_change'
    model = User
    fields = ['email']


class UserDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'users.can_delete'
    model = User
    success_url = reverse_lazy('user-list')
