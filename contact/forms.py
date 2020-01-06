from django import forms
from .models import MessageMe


class MessageForm(forms.ModelForm):
    email=forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control'}),
    )
    subject= forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    message= forms.CharField(
        max_length=500, required=False,
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    


    class Meta:
        model= MessageMe
        fields= {
            'email':'Email',
            'subject':'Subject',
            'message':'Message'
        }