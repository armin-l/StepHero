from django.contrib import admin
from django.urls import path
from users.views import google_fit_connect, google_fit_callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('google-fit/connect/', google_fit_connect, name='google_fit_connect'),
    path('google-fit/callback/', google_fit_callback, name='google_fit_callback'),
]