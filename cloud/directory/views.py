from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Folder, File
from django.views import View


class FolderView(View):
    template_name = "directory/folder.html"

    def get(self, request, path) -> HttpResponse:
        this_folder = get_object_or_404(Folder, name=path)
        children_folders = this_folder.children.all()
        files = this_folder.file.all()
        context = {
            "folder": this_folder,
            "children_folders": children_folders,
            "files": files,
        }
        return render(request, self.template_name, context)
