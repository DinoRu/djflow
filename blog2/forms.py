
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Commentaire....', 
                'style': 'max-width: 100%;',
            })
        }

    # Overriding default from settings and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Enter name', 'class':'form-control',}
        self.fields['email'].widget.attrs = {'placeholder': 'Enter email', 'class':'form-control'}
        