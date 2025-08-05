from django.shortcuts import render
from rest_framework import generics, permissions

from rest_framework.permissions import IsAuthenticated
from .models import Habit, HabitRecord
from .serializers import (
    HabitSerializer,
    HabitRecordSerializer,
    UserRegistrationSerializer,
)
from django.contrib.auth.models import User


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitDetailVewi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        habit_id = self.kwargs["habit_id"]
        return HabitRecord.objects.filter(
            habit__id=habit_id, habit__owner=self.request.user
        )

    def perform_create(self, serializer):
        habit_id = self.kwargs["habit_id"]
        habit = Habit.objects.get(id=habit_id, owner=self.request.user)
        serializer.save(habit=habit)


class HabitRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HabitRecord.objects.filter(habit__owner=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
