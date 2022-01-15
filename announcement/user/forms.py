from django.forms import ModelForm, TextInput, Textarea, PasswordInput, EmailInput, ImageField, FileInput

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'email', 'avatar']
        # widgets = {
        #     'login': TextInput(),
        #     'password': PasswordInput(),
        #     'email': EmailInput(),
        #     'avatar': FileInput()
        # }