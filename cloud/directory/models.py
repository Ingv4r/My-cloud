from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Folder(models.Model):
    name = models.CharField(verbose_name="Имя папки", max_length=100, unique=True)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    folders = models.ManyToManyField(to="self", blank=True, verbose_name="Папки")
    files = models.ForeignKey(to="File", blank=True, null=True, related_name="folder", on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Владелец", verbose_name="Folder owner")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'


class File(models.Model):
    name = models.CharField(verbose_name="Имя файла", max_length=100, unique=True, null=False)
    data = models.FileField(upload_to="datastore", null=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="file", verbose_name="Владелец файла")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
