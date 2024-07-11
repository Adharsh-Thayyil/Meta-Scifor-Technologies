from django import forms

class SimpleForm(forms.Form):
    name = forms.CharField(label='your name',max_length=100)
    email = forms.EmailField(label='your email')
    message = forms.CharField(widget=forms.Textarea,label='your message')