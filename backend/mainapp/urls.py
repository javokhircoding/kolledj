from django.urls import path

from .views import *


urlpatterns = [
    path('', TaskMixinView.as_view(), name='tasklist'),
    path('<slug:slug>/', TaskUpdate.as_view(), name='task-update'),
    path('<slug:slug>/delete/', TaskDelete.as_view(), name='task-delete')
]