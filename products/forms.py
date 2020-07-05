from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={
                                "placeholder": "your title name"
                            }))

    description = forms.CharField(required=False,
                                widget= forms.Textarea(attrs={
                                "placeholder": "your description",
                                "class": "form__input textarea",
                                "id": "description__input",
                                "row": "20",
                                "col": "30"
    }))

    price = forms.DecimalField(initial=199.99)
    email = forms.EmailField()
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "thong" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "2000" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("ca"):
            raise forms.ValidationError("This is not a valid email")
        return email
