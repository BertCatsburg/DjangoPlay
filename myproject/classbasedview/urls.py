from django.urls import path
from .views import MyView

urlpatterns = [
    path("a/", MyView.as_view(), name="a"),
]
