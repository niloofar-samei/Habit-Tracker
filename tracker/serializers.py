from rest_framework import serializers
from .models import Habit, HabitRecord
from django.contrib.auth.models import User


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "name", "owner", "created_at"]
        read_only_fields = ["id", "owner", "created_at"]


class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = ["id", "habit", "date", "completed"]
        read_only_fields = ["id"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

        def create(self, validated_data):
            # We do this to override create() to hash the password
            return User.objects.create_user(**validated_data)
