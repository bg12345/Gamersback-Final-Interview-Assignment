from rest_framework import serializers
from .models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True,required=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True,required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name','last_name','college_name','password', 'password2']

    def save(self, request, *args, **kwargs):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            college_name=self.validated_data['college_name']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user