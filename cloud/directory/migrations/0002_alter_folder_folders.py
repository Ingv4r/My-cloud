# Generated by Django 5.0.2 on 2024-02-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("directory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="folder",
            name="folders",
            field=models.ManyToManyField(
                blank=True, to="directory.folder", verbose_name="Папки"
            ),
        ),
    ]