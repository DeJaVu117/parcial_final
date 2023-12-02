from django import forms
from .models import Nota

class NotasForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Nota

        fields = [
            'titulo',
            'nota',
        ]

        labels = {
            'titulo':'titulo',
            'nota':'nota',
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','rows':3}),
            'nota':forms.NumberInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(NotasForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}