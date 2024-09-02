from django import forms

class ContactForm(forms.Form):
    users_name = forms.CharField(max_length=255)
    users_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
