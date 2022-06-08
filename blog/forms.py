from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content", "summary", "image", "is_published", "category")
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "content": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "summary": forms.Textarea(attrs={
                "class": "form-control"
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
        }

