from django.urls import path
from .views import register, user_login, group_statistics, leaderboard, create_group

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('group/<int:group_id>/statistics/', group_statistics, name='group_statistics'),
    path('group/<int:group_id>/leaderboard/', leaderboard, name='leaderboard'),
    path('group/create/', create_group, name='create_group'),
]