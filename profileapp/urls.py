from django.urls import path
from .views import MyProfile

urlpatterns = [
    path('', MyProfile.as_view(), name='Profile')
]