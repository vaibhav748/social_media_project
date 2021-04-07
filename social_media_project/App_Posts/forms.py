from django import forms
from App_Posts.models import Post


class PostForm(forms.ModelForm):
    caption = forms.CharField(max_length=254, label="",
                              widget=forms.TextInput(attrs={'placeholder': "Caption"}))

    class Meta:
        model = Post
        fields = ('image', 'caption')
