from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def file_size(value):
    if value.file.size > 5 * 1024 * 1024:
        raise ValidationError('Max file size is 5.00 MB')
