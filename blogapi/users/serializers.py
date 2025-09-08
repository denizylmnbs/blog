from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, min_length=8, validators=[validate_password], style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2']
        read_only_fields = ['id']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        # password2'yi at
        validated_data.pop('password2', None)
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NzQxMzI1MiwiaWF0IjoxNzU3MzI2ODUyLCJqdGkiOiJkYmQxYjVkYjNmNTc0NGVmOWEzM2RlNmFhMzUzYzIxNyIsInVzZXJfaWQiOiIyIn0.gaQxI9ZbX2XQ8ozL-OHbzZgZOSWzfsIt54as0PFfH8Q",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MzI3MTUyLCJpYXQiOjE3NTczMjY4NTIsImp0aSI6IjM5NzYwM2E5OWIxMzQ0ZjE5ZGU4N2QxMmRjMmMyZjM0IiwidXNlcl9pZCI6IjIifQ.JJGlFCLtur49NwbCwoJ6cT6HigosHtHJMV1-UpxLqS0"
}

{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MzI3NzE0LCJpYXQiOjE3NTczMjc0MTQsImp0aSI6IjI4ZmI2YWQ4Njg3YzQyMzFiZWI1NTBhZWFiMTE0NzA3IiwidXNlcl9pZCI6IjIifQ.M-GEdIw2plDcUs7gpj9mYNVYwANpH6WIPZ60urP-FW8"
}