from django.urls import path
from . import views
urlpatterns = [
    # Declares the pattern for the sign up page
    path('gkSignUp/', views.signup, name="gkSignUp"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]