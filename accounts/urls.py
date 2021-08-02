from django.urls import path

from .views import AccountPasswordChangeView, AccountRegistrationView, AccountLoginView, AccountLogoutView, AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('password/', AccountPasswordChangeView.as_view(), name='password'),
    path('profile_update/', AccountUpdateView.as_view(), name='profile_update'),
]