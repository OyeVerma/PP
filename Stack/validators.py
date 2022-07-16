from django.core.exceptions import ValidationError

def validate_title(value):
    if value in ['', ' ', 'new']:
        raise ValidationError('this title is not allowed'.title())
    else:
        return value.strip()