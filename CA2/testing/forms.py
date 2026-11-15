from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField()
    age = forms.IntegerField(min_value=1, max_value=120, required=False)
    message = forms.CharField(widget=forms.Textarea, help_text='Max 500 chars')



