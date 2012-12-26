from django import forms
from pastebin.apps.models import Paste

class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
