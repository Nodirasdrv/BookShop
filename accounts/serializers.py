from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

USER_TYPE_CHOICES = (
    (1, 'admin'),
    (2, 'reader'),
)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'user_type')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if not user.exists:
            raise ValidationError('email exists')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password2 != password:
            raise ValidationError('passwords do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if not user.exists():
            raise ValidationError('email does not exist')
        return value

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        print(user.is_active)
        if user and user.is_active:

            refresh = RefreshToken.for_user(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)
        return attrs
