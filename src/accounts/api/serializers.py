from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import User
from .utils import domain_list
import re
from better_profanity import profanity


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer serializes user data - username , email , token
    """

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "token")

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializes User registration data
    """

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    message = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2",
            "message",
            "token",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering, you can login now !"

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        mail_head = value.split("@")[0]
        mail_end = value.split("@")[1]
        if qs.exists():
            raise serializers.ValidationError(
                "An account with this email already exists"
            )
        if profanity.contains_profanity(mail_head):
            raise serializers.ValidationError(
                "The email must not contain any cuss word"
            )
        # elif re.match("[a-zA-Z]+", str(mail_head)):
        #     raise serializers.ValidationError(
        #         "Email should be consisting of name"
        #     )
        elif mail_end in domain_list:
            raise serializers.ValidationError(
                "Email should not be company email"
            )
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This username is unavailable")
        # if re.match("^[a-zA-Z]", str(value)):
        #     raise serializers.ValidationError(
        #         "Username should be consisting of name"
        #     )
        elif profanity.contains_profanity(value):
            raise serializers.ValidationError(
                "The username must not contain any cuss word"
            )
        return value

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.pop("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        user_obj = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user_obj.set_password(validated_data.get("password"))
        user_obj.is_active = True
        user_obj.save()
        return user_obj
