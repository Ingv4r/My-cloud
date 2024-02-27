from django import template
from ..models import Folder
register = template.Library()


@register.inclusion_tag('directory/folder.html', takes_context=True)
def show_folder(context):
    folders = Folder.objects.filter(level=0)
    return {
        "folders": folders,
    }