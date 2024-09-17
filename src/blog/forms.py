from django import forms

from .models import Pessoa


class UserForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(
                attrs={"type": "text", "maxlength": 100, "placeholder": "Arlon Madeira"}
            ),
            "idade": forms.TextInput(
                attrs={"type": "number", "min": 0, "placeholder": "28"}
            ),
            "cpf": forms.TextInput(
                attrs={"type": "text", "maxlength": 14, "placeholder": "000.000.000-00"}
            ),
        }
