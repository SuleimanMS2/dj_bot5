from django.urls import path

from .views import Master

urlpatterns = [
    path('', Master.as_view())
]