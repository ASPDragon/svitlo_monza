from django import forms

from contact_us.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs  # fix model name later if you rename
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Электронная почта"}),
        }