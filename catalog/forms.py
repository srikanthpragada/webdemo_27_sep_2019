from django import forms


class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    price = forms.IntegerField(required=False)
