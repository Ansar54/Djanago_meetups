from django import forms
from .models import Participant

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            
        }),
        error_messages={
            'required': 'Email field is required',
            'invalid': 'Enter a valid email address',
        }
    )

    class Meta:
        model = Participant
        fields = ['email']
