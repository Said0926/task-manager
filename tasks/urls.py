from django.urls import path
from . import views
from .views import user_login, user_logout

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create-task/', views.CreateTask.as_view(), name='create_task'), 
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'), 
    path('register/', views.Register.as_view(), name='register' ),
    
]