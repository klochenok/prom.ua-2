from django.forms import ModelForm

from .models import Name


class NameForm(ModelForm):

    def clean_name(self):
        data = self.cleaned_data['name']
        return data

    class Meta:
        model = Name
        fields = ('name',)
