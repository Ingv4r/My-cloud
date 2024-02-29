from django.urls import path

from .views import FolderView

urlpatterns = [
    path('folders/<path:path>', FolderView.as_view(), name='folder'),
]
