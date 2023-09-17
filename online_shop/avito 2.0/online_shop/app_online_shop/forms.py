from django import forms
from django.db import models
from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxInput, FileInput
from .models import OnlineShop

## Класс формы для полчения объявления унаследованный от Forms
## Закомментирован что бы переделать на класс унаследованный от ModelForm
# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control form-control-lg"}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': "form-control form-control-lg"}))
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': "form-check-input"}), required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control form-control-lg"}))

## Класс формы для полчения объявления унаследованный от ModelForms
class AdvertisementModelForm(ModelForm):
    class Meta:
        model = OnlineShop
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': TextInput(attrs={'class': "form-control form-control-lg"}),
            'description': Textarea(attrs={'class': "form-control form-control-lg"}),
            'price': NumberInput(attrs={'class': "form-control form-control-lg"}),
            'auction': CheckboxInput(attrs={'class': "form-check-input"}),
            'image': FileInput(attrs={'class': "form-control form-control-lg"})
        }
    
    # Проверка значения поля title
    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise ValueError('Заголовок не может начинаться с вопросительного знака.')
        return data