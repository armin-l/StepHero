from django.contrib import admin
from django.urls import path
from users.views import group_statistics, leaderboard

from users.views import group_statistics, leaderboard, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/<int:group_id>/statistics/', group_statistics, name='group_statistics'),
    path('group/<int:group_id>/leaderboard/', leaderboard, name='leaderboard'),
    path('login/', user_login, name='login')
]