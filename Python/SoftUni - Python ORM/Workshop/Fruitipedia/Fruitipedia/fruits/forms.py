from django import forms
from Fruitipedia.fruits.models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter a category'})
    )

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAddForm(CategoryBaseForm):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'URL Image'}),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Nutrition number'}),
        }

    def __init__(self, *args, **kwargs):
        super(BaseFruitForm, self).__init__(*args, **kwargs)
        # Remove labels by setting them to empty strings
        for field in self.fields.values():
            field.label = ''


class AddFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super(DeleteFruitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

        self.fields['category'].widget.attrs['disabled'] = True

