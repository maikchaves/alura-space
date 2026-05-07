from django import forms
from gallery.models import Photograph

#o Django ajuda a criar formulários baseado no Model
class PhotographForm(forms.ModelForm):
    class Meta:
        model = Photograph
        exclude = ['active']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'category': 'Categoria',
            'description': 'Descrição',
            'photo_path': 'Imagem',
            'date_upload': 'Data de Upload',
            'user': 'Usuário',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo_path': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_upload': forms.DateInput(format='%Y-%m-%d', 
                                           attrs={
                                                'class': 'form-control', 
                                                'type': 'date' 
                                            }),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }