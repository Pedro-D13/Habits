from django.urls import path

from todolist.views import *


app_name = 'tdl'
urlpatterns = [
    path('tdl/', TDL_ListView.as_view(), name='tdl_list'),
    path('tdl/add/', TDLCreateView.as_view(), name='tdl_create'),
    path('tdl/<int:pk>/update', TDLUpdateView.as_view(), name='tdl_update'),
    path('tdl/<int:pk>/delete', TDLDeleteView.as_view(), name='tdl_delete'),
]
