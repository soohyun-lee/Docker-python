from django.urls import path
from .views import Contents

urlpatterns = [
    path('/contents', Contents.as_view())
]
