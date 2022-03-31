from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not all(ch.isalpha for ch in value):
        raise ValidationError('Value must contain only letters!')
