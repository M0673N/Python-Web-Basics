from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator


def name_validator(value):
    if value != value.upper():
        raise forms.ValidationError('The name must start with an uppercase letter.')


def age_validator(value):
    if value < 0:
        raise forms.ValidationError('The age cannot be less than zero.')


def email_validator(value):
    if '.' not in value or '@' not in value:
        raise forms.ValidationError('Enter a valid email.')


def password_validator(value):
    if value.isalnum():
        raise forms.ValidationError('Enter a valid password.')


class DemoForm(forms.Form):
    name = forms.CharField(validators=[name_validator, MaxLengthValidator(6)])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[age_validator])
    email = forms.EmailField(widget=forms.EmailInput, validators=[email_validator])
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8), password_validator])
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(widget=forms.HiddenInput,
                                  validators=[MaxLengthValidator(0, message='This form was created by a bot')],
                                  required=False)
