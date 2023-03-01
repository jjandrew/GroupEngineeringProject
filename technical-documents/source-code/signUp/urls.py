from django.urls import path
from .views import signup

urlpatterns = [
    # Declares the pattern for the sign up page
    path('signup/', signup, name="signup"),
]