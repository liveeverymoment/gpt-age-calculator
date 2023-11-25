from django.urls import path
from .views import event_age

urlpatterns = [
    path('event/',event_age,name='event_age'),
]