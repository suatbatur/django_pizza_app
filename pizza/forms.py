from django import  forms
from django.forms import fields
from .models import PizzaApp


class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaApp
        fields = "__all__"