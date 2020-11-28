from django import forms


class HomeForm(forms.Form):
    post = forms.CharField(max_length=255)
