from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(max_length=10)
    description = forms.CharField(widget=forms.Textarea)
