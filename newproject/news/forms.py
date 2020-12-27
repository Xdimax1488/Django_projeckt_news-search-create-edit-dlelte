from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', '_category', 'title', 'text_news', 'text_title']
