from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import Folder
register = template.Library()


# @register.inclusion_tag('directory/folder.html', takes_context=True)
def show_folder():
    folders = Folder.objects.filter(level=0)
    return {
        "folders": get_folder(folders),
    }
