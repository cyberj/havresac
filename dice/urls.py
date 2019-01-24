from django.urls import path
from dice import api

urlpatterns = [
    path('d2', api.d2),
    path('d4', api.d4),
    path('d6', api.d6),
    path('d8', api.d8),
    path('d10', api.d10),
    path('d12', api.d12),
    path('d20', api.d2),
    path('d100', api.d100),
]
