from django.urls import path

from contact_us import views

urlpatterns = [
    path("", views.contact_us, name="contact_us"),
]