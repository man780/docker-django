from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=150)
    menu_url = models.URLField(null=True)
