from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('folders', TemplateView.as_view(template_name="home.html")),
]