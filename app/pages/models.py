from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    STATUS_CHOICES = [
        (1, 'Available'),
        (0, 'Unavailable'),
        (2, 'Draft'),
    ]
    sequence = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    menu_id = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name="Status")
    created_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a slug when saving the page
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ["sequence", "-id",]

    def __str__(self):
        return self.title


class Page(models.Model):
    STATUS_CHOICES = [
        (0, 'Unavailable'),
        (1, 'Available'),
        (2, 'Draft')
    ]
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    menu_id = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)
    small_content = models.CharField(max_length=255, null=True, blank=True, default=None)
    content = models.TextField(null=True, blank=True, default=None)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name="Status")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["-id",]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug when saving the page
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
