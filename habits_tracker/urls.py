from django.urls import path

from habits_tracker import views

APP_NAME = "habits"
urlpatterns = [
    path('', views.Home, name='homepage'),
    # path('<int:pk>/', views.HbaitDetailView.as_view(), )
]
