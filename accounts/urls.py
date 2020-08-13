from django.urls import path
from .views import SignUpView, UserProfile, UserUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profil/', UserProfile.as_view(), name='user_profile'),
    path('user_update_profile/', UserUpdate.as_view(), name='user-update-profile'),
]
