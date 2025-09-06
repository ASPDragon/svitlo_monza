from django import forms
from .models import Consultation   # ⚠️ typo here, should be "Consultation"

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation  # fix model name later if you rename
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Телефон"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': "Повідомлення"}),
        }
