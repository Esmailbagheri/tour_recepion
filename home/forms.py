from django import forms
from .models import Post, Comment

class CreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titel', 'body')
        labels = {
            'titel': 'Titel'
        }


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'body': 'سوالات'
        }

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'body': 'ارسال نظر'
        }

class SearchForm(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'search'}))

