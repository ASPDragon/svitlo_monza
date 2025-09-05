from django.urls import path

from consultation import views

urlpatterns = [
    path("", views.consultation, name="consultation"),
]