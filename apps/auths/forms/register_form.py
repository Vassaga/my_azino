from django import forms 

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Почта", max_length=200)
    nickname = forms.CharField(label="Ваш ник", max_length=100)
    password = forms.CharField(label="Пароль", min_length=6)
    password = forms.CharField(label="Повторите пароль", min_length=6)