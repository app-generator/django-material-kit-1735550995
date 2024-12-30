# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Nota(models.Model):

    #__Nota_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    cuerpo = models.CharField(max_length=255, null=True, blank=True)
    fecha creacion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha actualizacion = models.CharField(max_length=255, null=True, blank=True)

    #__Nota_FIELDS__END

    class Meta:
        verbose_name        = _("Nota")
        verbose_name_plural = _("Nota")



#__MODELS__END
