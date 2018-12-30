from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',]

        labels = {'title': 'Title',
                  'text': 'Text' ,}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                   'text': forms.Textarea(attrs={'class': 'form-control'}),}