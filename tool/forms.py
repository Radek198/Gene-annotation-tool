from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.Textarea)


class DataAddForm(forms.Form):
    input_data = forms.CharField(max_length=255)