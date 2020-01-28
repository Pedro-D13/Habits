from django.urls import path

from .views import *

app_name = 'habits'
urlpatterns = [
    path('', PersonView.as_view(), name='person_detail')
    # path('<int:pk>/', views.HbaitDetailView.as_view(), )
]
