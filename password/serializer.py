from rest_framework import serializers


number_length = range(1, 100)


class PasswordSerializer(serializers.Serializer):
    password_length = serializers.ChoiceField(choices=number_length)
    uppercase = serializers.BooleanField()
    numbers = serializers.BooleanField()
    symbols = serializers.BooleanField()
