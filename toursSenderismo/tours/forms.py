from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['nombre', 'descripcion', 'duracion', 'precio']

from django import forms
from .models import Reseña

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['texto', 'rating']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Haznos saber tu opinión'}),
            'rating': forms.RadioSelect(attrs={'class': 'star-rating'}, choices=[(i, str(i)) for i in range(1, 6)]),
        }
