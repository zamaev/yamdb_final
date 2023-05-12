from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from users.validators import username_is_not_me_validators


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. '
                   'Letters, digits and @/./+/-/_ only.'),
        validators=(
            UnicodeUsernameValidator(),
            username_is_not_me_validators,
        ),
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=15,
        choices=ROLE_CHOICES,
        default=USER,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            models.UniqueConstraint(
                fields=('email',),
                name='unique_email',
            ),
        )

    @property
    def is_user(self):
        return (not self.is_admin
                and not self.is_moderator
                and self.role == self.USER)

    @property
    def is_moderator(self):
        return (not self.is_admin
                and (self.is_staff
                     or self.role == self.MODERATOR))

    @property
    def is_admin(self):
        return (self.is_superuser
                or self.role == self.ADMIN)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.ADMIN
        if self.is_admin or self.is_moderator:
            self.is_staff = True
        super().save(*args, **kwargs)
