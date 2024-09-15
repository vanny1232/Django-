from django import forms
from shop.models import product


class ProductForm(forms.ModelForm):

    class Meta:
        model = product
        fields = ['name', 'catagory','price','valume','disciptions','img']