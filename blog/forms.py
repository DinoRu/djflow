from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
   
   class Meta:
       model = Comment
       fields = ('author', 'email', 'body')
       widgets = {
            'author':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom...'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email...'}),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Commentaire...'}),
       }