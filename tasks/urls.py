from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('update_task/<str:pk_test>',views.update_task,name='update-task'),
    path('delete_task/<str:pk_test>',views.delete_task,name='delete-task'),
]