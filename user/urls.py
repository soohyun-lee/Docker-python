from django.urls import path
from .views import SignUp

urlpatterns = [
    path('/account', SignUp.as_view())
]

