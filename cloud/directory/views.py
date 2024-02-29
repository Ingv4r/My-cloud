from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Folder
from django.views import View


class FolderView(View):
    template_name = "folder.html"

    def get(self, request, path) -> HttpResponse:
        folder = get_object_or_404(Folder, name=path)
        return render(request, self.template_name, {'folder': folder})

