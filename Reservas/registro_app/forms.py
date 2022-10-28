from django import forms
from registro_app.models import reserva

class FormRegistro(forms.ModelForm):
   
    cantidad = forms.IntegerField(min_value = 1, max_value = 15)
    
    observacion = forms.CharField(required=False)

    class Meta:
        model = reserva
        fields = ('nombre','fono','fechareserva','hora','cantidad','estado','observacion')




