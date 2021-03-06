from django import forms
from .models import PortfolioItem, Images

class PortfolioItemForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    description = forms.CharField(max_length=245, label="Item Description")

    class Meta:
        model = PortfolioItem
        fields = ('title', 'description', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )