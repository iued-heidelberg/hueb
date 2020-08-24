from django.db import models
from hueb.apps.hueb20.models import HUEB20, HUEB_APPLICATIONS


class CulturalCircle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="Name of the cultural circle")
    description = models.TextField(null=True, blank=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)

    def __str__(self):
        if self.name is None:
            return " "
        return self.name
