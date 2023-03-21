from django.urls import path
from . import views
urlpatterns = [
    # Declares the pattern for the sign up page
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]