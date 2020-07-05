from django import forms
from .models import Article

class BlogForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder": "enter your title"
    }))

    content = forms.CharField(widget= forms.Textarea(attrs={
        "placeholder": "enter content here",
        "row": "40",
        "col": "30"
    }))
    class Meta:
        model = Article
        fields = ['title', 'content', 'active']
