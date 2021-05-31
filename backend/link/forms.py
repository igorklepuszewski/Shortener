from link.models import Link
from django import forms


class LinkForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Paste a long url",
        "id": "input"}))

    class Meta:
        model = Link
        fields = ('long_url',)
