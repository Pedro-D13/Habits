from django.urls import path
from .views import GoalCreateView
# GoalListView
from habits_tracker import views

APP_NAME = "habits"
urlpatterns = [
    path('', views.Home, name='homepage'),
    path('create/add/', GoalCreateView.as_view(), name='goal_create'),
    # path('list/', GoalListView.as_view(), name='goal_list'),
    # path('<int:pk>/', views.HbaitDetailView.as_view(), )
]
