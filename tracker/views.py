from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import permissions
from .models import Habit, HabitRecord
from .serializers import HabitSerializer, HabitRecordSerializer


class HabitListCreateView(generics.ListCreateView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
