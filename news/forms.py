from django import forms
class CommentForm(forms.Form):
    text = forms.CharField(max_length=300)
class NewsArticleForm(forms.Form):
    title = forms.CharField(max_length=300)
    text = forms.CharField(max_length=20000)
    img = forms.ImageField()
