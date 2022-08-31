from django.forms import ModelForm
from django.forms import TextInput

from .models import Document


class CustomForm(ModelForm):
    class Meta:
        model = Document
        fields = ['type_doc', 'addressee', 'doc_direction']

        widgets = {
            "doc_direction": TextInput(attrs={
                'placeholder': 'Назначение справки'
            })
        }
