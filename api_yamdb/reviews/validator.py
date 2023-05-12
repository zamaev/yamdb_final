from django.core.exceptions import ValidationError
from django.utils import timezone


def title_year_validator(value):
    """Год не болше текущего."""
    if value > timezone.now().year:
        raise ValidationError(f'Значение {value} больше текущего года.')
