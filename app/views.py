from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from .forms import NameForm
from .models import Name


class NameCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = NameForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name').lower()
            name_exists = Name.objects.filter(name=name).exists()

            if name_exists:
                context = {
                    'message': 'Name already exists. Try another one:',
                    'form': form
                }
                return render(request, 'already-exists.html', context)
            else:
                Name.objects.create(name=name)
                context = {
                    'message': 'Name was successfully added!'
                }
                return render(request, 'success.html', context)
        context = {
            'message': 'Field <name> is not valid.',
            'form': form
        }
        return render(request, 'index.html', context)


class RandomNamesListView(ListView):
    queryset = Name.objects.all().order_by('?')[0:3]

    def get(self, request, *args, **kwargs):
        queryset = Name.objects.all().order_by('?')[0:3]
        context = {
            'random_names': list(obj.name for obj in queryset)
        }
        return render(request, 'random-names.html', context)


class NameDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        form = NameForm()
        context = {
            'form': form
        }
        return render(request, 'delete-name.html', context)

    def post(self, request, *args, **kwargs):
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name').lower()
            name_exists = Name.objects.filter(name=name).exists()

            if name_exists:
                Name.objects.filter(name=name).delete()
                context = {
                    'message': 'Name was successfully deleted!'
                }
                return render(request, 'success.html', context)
            else:
                context = {
                    'message': 'Name is not exists. Try another one:',
                    'form': form
                }
                return render(request, 'delete-name.html', context)
        context = {
            'message': 'Field <name> is not valid.',
            'form': form
        }
        return render(request, 'delete-name.html', context)
