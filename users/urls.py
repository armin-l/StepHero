from django.urls import path
from .views import register, group_statistics, leaderboard

urlpatterns = [
    path('register/', register, name='register'),
    path('group/<int:group_id>/statistics/', group_statistics, name='group_statistics'),
    path('group/<int:group_id>/leaderboard/', leaderboard, name='leaderboard'),
]