from django.urls import path
from .views import GoalCreateView, GoalListView, GoalUpdateView, GoalDeleteView

from habits_tracker import views

APP_NAME = "habits"
urlpatterns = [
    path('', views.Home, name='homepage'),
    path('goal/add/', GoalCreateView.as_view(), name='goal_create'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete', GoalDeleteView.as_view(), name='goal_delete'),

]
