from django.urls import path
from . import api

urlpatterns = [
    path('register/', api.register, name='register'),
    path('me/', api.currentUser, name='current_user'),
    path('me/update/', api.updateUser, name='update_user'),
]
