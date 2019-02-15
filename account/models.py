import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .manager import UserManager


# Create your models here.


class PhoneField(models.CharField):
    description = 'User phone number'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
    )
    phone_number = PhoneField(
        verbose_name=_('전화번호')
    )
    date_of_birth = models.DateField(verbose_name=_('생년월일'))
    username = None
    first_name = None
    last_name = None
    name = models.CharField(_('name'), max_length=30, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'date_of_birth']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.name

    def get_short_name(self):
        return "%s 회원님" % self.name


def get_time_limit():
    return timezone.now() + timezone.timedelta(hours=1)


class RegisterLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    register_until = models.DateTimeField(default=get_time_limit)
    register_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = '가입 링크'
        verbose_name_plural = '가입 링크(들)'

    def __str__(self):
        return self.user.name
