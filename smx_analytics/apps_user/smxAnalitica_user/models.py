""" Modelo de Usuario """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

# Django
from django.db import models
from django.contrib.auth.models import User
from decouple import config

class userArea(models.Model):
    nombre = models.CharField(max_length=250, unique=True)

    class Meta:
        db_table = 'userArea'

    def userAreaDeafult(self):
        userdb = userArea()
        userdb.nombre = "defaulData"
        userdb.save()
        return userdb.id

    def userAreaSuperUsuario(self):
        userdb = userArea()
        userdb.nombre = "SuperUsuario"
        userdb.save()
        return userdb.id

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class UsuarioManager(BaseUserManager):
    def create_user(
        self,
        usuario,
        email,
        nombre,
        tipo_autenticacion,
        versiones_piloto,
        notificar,
        password=None
    ):

        dato = userArea.objects.filter(nombre="SuperUsuario")

        #dato = userArea.objects.get(nombre="SuperUsuario")
        if dato:
            id = dato[0].id
        else:
            id = userArea.userAreaSuperUsuario(self)
            print(id)
        if not email:
            raise ValueError('Campo de Correo Obligatorio')

        usuario_obj = self.model(
            usuario=usuario,
            email=email,
            nombre=nombre,
            tipo_autenticacion=tipo_autenticacion,
            versiones_piloto=versiones_piloto,
            notificar=notificar,
        )
        usuario_obj.area = userArea.objects.get(pk=id)
        usuario_obj.set_password(password)
        usuario_obj.save(using=self._db)
        return usuario_obj

    def create_superuser(
        self,
        usuario,
        email,
        nombre,
        tipo_autenticacion,
        versiones_piloto,
        notificar,
        password
    ):
        usuario_obj = self.create_user(
            usuario=usuario,
            email=email,
            nombre=nombre,
            tipo_autenticacion=tipo_autenticacion,
            versiones_piloto=versiones_piloto,
            notificar=notificar,
        )
        usuario_obj.is_superuser = True
        usuario_obj.activo = True
        usuario_obj.is_staff = True
        usuario_obj.set_password(password)
        usuario_obj.save(using=self._db)
        return usuario_obj


class user(AbstractBaseUser, PermissionsMixin):

    SISTEMA = 1
    AD = 2

    TIPO_AUTT = (
        (SISTEMA, "Sistema"),
        (AD, "Active Directory")
    )

    area = models.ForeignKey(userArea, on_delete=models.PROTECT, null=False, blank=False, default=1)
    usuario = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=250)
    tipo_autenticacion = models.IntegerField(choices=TIPO_AUTT, default=SISTEMA, null=False, blank=False)
    versiones_piloto = models.BooleanField(default=False,)
    notificar = models.BooleanField(default=False,)
    activo = models.BooleanField(default=False,)
    is_staff = models.BooleanField(default=False,)
    is_superuser = models.BooleanField(default=True,)
    foto = models.ImageField(upload_to='uploads/user', null=True, blank=True)
    token = models.CharField(max_length=100)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = [
        'nombre',
        'email',
        'tipo_autenticacion',
        'versiones_piloto',
        'notificar',
    ]

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
