from django import forms
from .models import MessageMe
from captcha.fields import CaptchaField


class MessageForm(forms.ModelForm):
    email=forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','required':'True'}),
    )
    subject= forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject','required':'True'}),
    )
    message= forms.CharField(
        max_length=500, required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Enter your message','required':'True'}),
    )
    captcha= CaptchaField()



    class Meta:
        model= MessageMe
        fields= {
            'email':'Email',
            'subject':'Subject',
            'message':'Message'
        }