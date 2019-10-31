from django import forms
from .models import Author


class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    price = forms.IntegerField(required=False)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'email', 'mobile']
