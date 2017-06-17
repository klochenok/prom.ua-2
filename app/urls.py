from django.conf.urls import url

from .views import NameCreateView, RandomNamesListView, NameDeleteView

urlpatterns = [
    url(r'^$', NameCreateView.as_view(), name='index'),
    url(r'^random/$', RandomNamesListView.as_view(), name='random_names'),
    url(r'^delete_name/$', NameDeleteView.as_view(), name='delete-name'),
]