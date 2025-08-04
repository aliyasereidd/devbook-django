from django import forms
from .models import Book,Category
class categoryforms(forms.ModelForm):
    class Meta:
        model =Category
        fields =['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'})



        }





class bookforms(forms.ModelForm):
    class Meta:
        model =Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'rental_price_daily',
            'rental_period',
            'total_rental',
            'status',
            'category',

            
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم الكتاب'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المؤلف'}),

            'photo_book': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.ClearableFileInput(attrs={'class': 'form-control'}),

            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'عدد الصفحات'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'سعر الكتاب'}),
            'total_rental':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'سعر الكتاب', 'id':'total'}),
            'rental_price_daily': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'السعر اليومي للإيجار', 'id':'rentalprice'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مدة الإيجار بالأيام', 'id':'rentperiod'}),

            'status': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

     

