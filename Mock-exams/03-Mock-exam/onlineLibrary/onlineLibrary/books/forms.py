from django import forms

from onlineLibrary.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime..'}),
        }
