from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from product.models import Product  


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'author','isbn13', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'isbn13': forms.TextInput(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border rounded-xl border-gray-400'
            })
        }