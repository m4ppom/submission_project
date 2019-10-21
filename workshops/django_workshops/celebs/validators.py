from django.core.exceptions import ValidationError


def validate_too_old(number):
    if number > 150:
        raise ValidationError(f'{number} 까지 살수 없', params=('number': number))


def validate_even(number):
    if number % 2:
        raise ValidationError(f'{number} is not even', params=('number': number))


def validate_too_young(number):
    if age < 20:
        raise ValidationError(f'미성년자 노노')