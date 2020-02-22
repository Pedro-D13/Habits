from django.urls import path
from .views import TDL_List


app_name = 'tdl'
urlpatterns = [
    path('tdl/', TDL_List.as_view(), name="tdl_list"),
]
