from django import forms

from recipes.app.models import Recipe


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs['label_suffix'] = ''
        super().__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time (Minutes)',
        }


class DeleteRecipeForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
