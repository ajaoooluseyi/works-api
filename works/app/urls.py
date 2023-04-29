from django.urls import path, include
from .views import (
    RegisterAPI,
    WorkApiView,
)


urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('works/', WorkApiView.as_view()),
]
