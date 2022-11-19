from rest_framework import serializers


class PruebaSerializer(serializers.Serializer):

    nombre = serializers.CharField(max_length=40, allow_null = False)
    apellidos =serializers.CharField (allow_null=False)