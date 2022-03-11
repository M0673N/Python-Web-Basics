import re

from django.core.exceptions import ValidationError


def alphanum_and_underscore_validator(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
