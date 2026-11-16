from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[MinLengthValidator(3)])
    email = forms.EmailField()
    rating = forms.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    comments = forms.CharField(widget=forms.Textarea)

    def clean_comment(self):
        c = self.cleaned_data['comment']
        if 'spam' in c.lower():
            raise forms.ValidationError("Comment nust not contain 'spam'.")
            return c



    