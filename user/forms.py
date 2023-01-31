from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django import forms
from django.urls import reverse_lazy


class BaseSignupForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2")

    def save(self, commit=True):
        user = super().save()
        user.active = False
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)

        return user


class BaseProfileForm(UserChangeForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="%s">this form</a>.'
        ) % reverse_lazy('account_change_password')
