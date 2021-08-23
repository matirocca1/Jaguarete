from django import forms

class ContactForm(forms.Form):
    nombre=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass