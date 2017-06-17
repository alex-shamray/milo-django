from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='user-list'),
    url(r'^add/$', views.UserCreateView.as_view(), name='user-add'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.UserDeleteView.as_view(), name='user-delete'),
    url(r'^(?P<pk>[0-9]+)/change/$', views.UserUpdateView.as_view(), name='user-change'),
]
