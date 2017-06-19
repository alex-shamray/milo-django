import csv

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import StreamingHttpResponse
from django.urls import reverse_lazy
from django.views import generic, View

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
    raise_exception = True
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'birthday']


class UserDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'users.can_delete'
    raise_exception = True
    model = User
    success_url = reverse_lazy('user-list')


class Echo(object):
    """
    An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """
        Write the value by returning it, instead of storing in a buffer.
        """
        return value


class UserExportView(View):
    """
    A view that streams a large CSV file.
    """

    def get(self, request, *args, **kwargs):
        def streaming_csv():
            pseudo_buffer = Echo()
            writer = csv.writer(pseudo_buffer)
            yield writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])

            users = User.objects.all()
            for user in users:
                rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
                yield writer.writerow([
                    user.username,
                    user.birthday,
                    '',
                    user.random_num,
                    '',
                ])

        response = StreamingHttpResponse(streaming_csv(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'
        return response
