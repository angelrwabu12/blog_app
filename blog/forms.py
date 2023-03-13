from django import forms
from .models import BlogItems

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogItems
        fields = ['blog_tittle', 'blog_description', 'blog_author', 'blog_image']