from django.urls import path
from accounts.views import (
    AccountNewestView,
    AccountView,
    LoginView,
    AccountIdView,
    AccountManagementView,
)

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<str:user_uuid>/", AccountIdView.as_view()),
    path("accounts/<str:user_uuid>/management/", AccountManagementView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", AccountNewestView.as_view()),
]
