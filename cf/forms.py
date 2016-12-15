from django import forms
from .models import Key, SafeBox


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ('description', 'document', 'safe_box', )


class SafeBoxForm(forms.ModelForm):
    class Meta:
        model = SafeBox
        fields = ('name', )
