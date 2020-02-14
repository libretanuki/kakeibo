from django import forms
from .models import Parent

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name']

    def save(self, commit=True):
        instance = super(ParentForm, self).save(commit=commit)

        if commit:
            instance.save()

        return instance

