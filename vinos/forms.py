from django import forms
from .models import Bodega, Vino, Reseña

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = '__all__'
        
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = '__all__'


