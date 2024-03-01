from django.contrib.auth import get_user_model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Folder(MPTTModel):
    name = models.CharField(verbose_name="Имя папки", max_length=100, unique=True)
    parent = TreeForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="folder", verbose_name="Владелец папки")

    def __str__(self):
        return str(self.name)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'


class File(models.Model):
    name = models.CharField(verbose_name="Имя файла", max_length=100, unique=True, null=False)
    data = models.FileField(upload_to="datastore", null=False)
    folder = models.ForeignKey(
        to=Folder,
        null=False,
        on_delete=models.CASCADE,
        related_name="file",
        verbose_name="Файл"
    )
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="file", verbose_name="Владелец файла")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
