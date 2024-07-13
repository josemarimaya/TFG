
from rest_framework import serializers
from .models import Usuario, Especialidad
from django.contrib.auth.hashers import make_password

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'nombre']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nombre', 'apellido', 'email', 'especialidades', 'equipos', 'is_active', 'is_staff', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)  # Encriptar la contraseña antes de guardar
        usuario = Usuario.objects.create(**validated_data)
        return usuario

    def update(self, instance, validated_data):
        # Actualizar campos según los datos validados
        instance.username = validated_data.get('username', instance.username)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.email = validated_data.get('email', instance.email)
        instance.especialidades.set(validated_data.get('especialidades', instance.especialidades.all()))
        instance.equipos.set(validated_data.get('equipos', instance.equipos.all()))
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        # Actualizar contraseña si se proporciona una nueva
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

