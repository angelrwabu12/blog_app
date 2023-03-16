from django import forms
from .models import BlogItems
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogItems
        fields = ['blog_tittle', 'blog_description', 'blog_author', 'blog_image']

class NewUserFrom(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=("username","email","password1","password2")

    def save(self,commit=True):
        user=super(NewUserFrom,self).save(commit==False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
