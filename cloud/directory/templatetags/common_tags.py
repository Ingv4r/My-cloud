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


def get_folder(items, folder: str = None, subfolder: list = None):
    menu = (
        list(items.filter(parent=None))
        if folder is None
        else list(items.filter(parent__name=folder))
    )
    try:
        menu.insert(menu.index(subfolder[0].parent) + 1, subfolder)
    except (IndexError, TypeError):
        pass
    try:
        return get_folder(items, items.get(name=folder).parent.name, menu)
    except AttributeError:
        return get_folder(items=items, subfolder=menu)
    except ObjectDoesNotExist:
        return menu


# @register.inclusion_tag("menu_app/menu.html")
def draw_menu(menu_name: str = None, menu_item: str = None):
    items = Folder.objects.all()
    return (
        {"menu": get_folder(items)}
        if menu_name == menu_item
        else {"menu": get_folder(items, menu_item)}
    )
