from django import forms


class Importer(forms.Form):
    file = forms.FileField()