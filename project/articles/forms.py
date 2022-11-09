from django import forms

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article']
        # fields = ['introduction', 'avatar', 'is_visable']