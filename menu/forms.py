from django import forms

from menu.models import Category
from accounts.validators  import allow_only_images_validators

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','description']
