from django import forms

class TeacherFD(forms.Form):
    question = forms.CharField(
        label='Ваш вопрос',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Напишите ваш вопрос здесь...',
            'class': 'form-control'
        }),
        required=True,
        max_length=1000
    )