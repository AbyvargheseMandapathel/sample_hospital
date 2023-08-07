from django.urls import path
from .views import RegisterView, CustomLoginView

app_name = 'authentication_app'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
