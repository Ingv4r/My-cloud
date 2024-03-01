from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Folder, File


class FolderMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Folder, FolderMPTTModelAdmin)
admin.site.register(File)
