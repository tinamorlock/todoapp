from django.urls import path

from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('<int:task_id>/complete/', views.complete, name='complete'),
    path('add/', views.add, name='add'),
    path('<int:task_id>/update/', views.update, name='update'),
    path('<int:task_id>/delete/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.auth_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
]