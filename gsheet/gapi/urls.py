from django.urls import path
from .views import GAPIView

urlpatterns = [
path('', GAPIView.as_view())
    
]