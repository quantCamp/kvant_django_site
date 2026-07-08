from django import forms

class TeacherFD(forms.Form):
    text = forms.CharField(label='Вопрос преподавателю', max_length=250, required=True) 