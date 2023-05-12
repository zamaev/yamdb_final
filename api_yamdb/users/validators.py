from django.core.exceptions import ValidationError


def username_is_not_me_validators(username):
    if username.lower() == 'me':
        raise ValidationError('Username cannot be "me"')
