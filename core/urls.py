from django.urls import path

from core.views import index, secret, ProfilePageView, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("secret/", secret, name="secret"),
    path("", index, name="home"),
]
