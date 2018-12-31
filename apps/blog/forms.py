from django import forms
from apps.blog.models import Post, Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',]

        labels = {'title': 'Title',
                  'text': 'Text' ,}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                   'text': forms.Textarea(attrs={'class': 'form-control'}),}



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
                  'name',
                  'description',
                  'posts']

        labels = {
                  'name':'Nombre BLog',
                  'description':'Informacion',
                  'posts':'Posts'}

        widgets = {
                   'name': forms.TextInput(attrs={'class':'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'posts': forms.CheckboxSelectMultiple(),}