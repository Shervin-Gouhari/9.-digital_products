from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    GENDER = (
        (_(''), 'unset'),
        (_('male'), 'male'),
        (_('female'), 'female')
    )
    user = models.OneToOneField(to=User, verbose_name=_("user"), on_delete=models.CASCADE)
    nick_name = models.CharField(_("nick name"), max_length=150, blank=True)
    avatar = models.ImageField(_("avatar"), blank=True)
    birthday = models.DateField(_("birthday"), null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=10, choices=GENDER, default='')
    province = models.ForeignKey(to=Province, verbose_name=_("province"), null=True, on_delete=models.SET_NULL)