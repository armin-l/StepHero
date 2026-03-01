from django.contrib import admin
from django.urls import path
from users.views import send_test_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-test-email/', send_test_email, name='send_test_email'),
]