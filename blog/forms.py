from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
        'title': forms.TextInput(label="Заголовок",attrs={'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug
