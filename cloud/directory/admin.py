from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Folder


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Folder, MenuItemMPTTModelAdmin)
