from django import forms

class NewsArticleForm(forms.Form):
    title = forms.CharField(max_length=300)
    text = forms.CharField(max_length=20000)
    img = forms.ImageField()


class NewComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Оставьте комментарий')