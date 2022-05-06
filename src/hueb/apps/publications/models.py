from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Publication(models.Model):
    file = models.FileField(upload_to="publications/")
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, blank=True, null=True
    )

    def download_link(self):
        if self.file:
            return mark_safe(f"<a href='{self.file.url}'>Download File</a>")
        else:
            return "No attachment"

    # download_link.allow_tags = True