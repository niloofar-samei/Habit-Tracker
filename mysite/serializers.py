from rest_framework import serializers
from .models import Habit, HabitRecord


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
