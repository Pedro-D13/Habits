from django.urls import path
from habits_tracker import views

from .views import (GoalCreateView, GoalListView,
                    GoalUpdateView, GoalDeleteView,
                    GoalDetailView)


app_name = "habits"
urlpatterns = [
    path('', views.Home, name='homepage'),
    path('goal/add/', GoalCreateView.as_view(), name='goal_create'),
    path('goal/list/', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/update', GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal/<int:pk>/delete', GoalDeleteView.as_view(), name='goal_delete'),
]
