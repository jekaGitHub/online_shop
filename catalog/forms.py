from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'):
            raise forms.ValidationError('Название содержит запрещённые слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'):
            raise forms.ValidationError('Описание содержит запрещённые слова')
        return cleaned_data