from django.urls import path

from todolist.views import (
    TDL_CreateView, TDLItemsListView,
    TDL_DeleteView, TDL_ListView,
    TDL_UpdateView, TDLItems_CreateView,
    TDLItems_DeleteView, TDLItem_UpdateView)


app_name = 'tdl'
urlpatterns = [
    # Path for Todolists
    path('tdl/', TDL_ListView.as_view(), name='tdl_list'),
    path('tdl/add/', TDL_CreateView.as_view(), name='tdl_create'),
    path('tdl/<int:pk>/update/', TDL_UpdateView.as_view(), name='tdl_update'),
    path('tdl/<int:pk>/delete/', TDL_DeleteView.as_view(), name='tdl_delete'),
    path('tdl/<int:pk>/', TDLItemsListView.as_view(), name="tdl_detail"),
    # Path
    path('tdi/add/<int:pk>/', TDLItems_CreateView.as_view(), name='tdi_create'),
    path('tdi/<int:pk>/delete/', TDLItems_DeleteView.as_view(), name='tdi_delete'),
    path('tdi/<int:pk>/update/', TDLItem_UpdateView.as_view(), name='tdi_update'),
]
