"""Usuario serializers."""


# Django Rest Framework
from rest_framework import serializers
import django_filters


from apps_user.smxAnalitica_user.models import (
    userArea,
    user,
)


class UserAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = userArea
        fields = (
           'id',
           'nombre',
        )


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)
    token = serializers.CharField(write_only=True,required=False)
    foto = serializers.ImageField(write_only=False,required=False)
    #area = serializers.CharField(write_only=False,required=False)
    usuario = serializers.CharField(write_only=False,required=False)
    email = serializers.CharField(write_only=False,required=False)
    nombre = serializers.CharField(write_only=False,required=False)
    versiones_piloto = serializers.BooleanField(write_only=False,required=False)
    notificar = serializers.BooleanField(write_only=False,required=False)
    activo = serializers.BooleanField(write_only=False,required=False)



    class Meta:
        model = user
        fields = (
            'id',
            'area',
            'usuario',
            'email',
            'nombre',
            'password',
            'versiones_piloto',
            'notificar',
            'activo',
            'foto',
            'token',
        )
    #def get_foto(self, obj, request):
        
        #print(obj.foto.url)
        #print(obj.foto.name)
        #return base_url

    def create(self, validated_data):
        user = super(UserSerializers, self).create(
            validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializers, self).update(
            instance,
            validated_data,
        )
