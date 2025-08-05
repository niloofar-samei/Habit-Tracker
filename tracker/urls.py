from django.urls import path
from .views import (
    HabitListCreateView,
    HabitDetailVewi,
    HabitRecordListCreateView,
    HabitRecordDetailView
)

urlpatterns = [
    path("habits/", HabitListCreateView.as_view(), name="habit-list-create"),
    path("habit/<int:pk>/", HabitDetailVewi.as_view(), name="habit-detail"),
    path("habit/<int:habit_id>/records/", HabitRecordListCreateView.as_view(), name="habit-records")
    path("records/<int:pk>", HabitRecordDetailView.as_view(), name="habit-record-detail")
]
