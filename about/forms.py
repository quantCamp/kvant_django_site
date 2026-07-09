from django import forms

class SchoolApplicationForm(forms.Form):
    parent_name = forms.CharField(label='Имя родителя', max_length=50, required=True)
    student_name = forms.CharField(label='Имя учащегося', max_length=50, required=True)
    student_age = forms.IntegerField(label='Возраст учащегося', required=True)
    phone = forms.CharField(label='Номер телефона', max_length=15, required=True)
    email = forms.EmailField(label='e-mail', required=True)
    achievements = forms.ImageField(label="Достижения")