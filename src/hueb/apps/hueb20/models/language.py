import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from translated_fields import TranslatedField

class Language(Reviewable):
    id = models.BigAutoField(primary_key=True)
    language = TranslatedField(models.CharField(max_length=255, null=True))
    language_temp = models.CharField(max_length=255, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    language_ref = models.OneToOneField(
        Legacy.Language,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="language_ref",
    )

    def __str__(self):
        if self.language is None:
            return " "
        return self.language

    def linked_name(self):
        url = reverse(
            "admin:hueb20_language_change",
            args=[self.id],
        )
        link = '<a href="%s">Language: %s</a>' % (url, str(self))
        return link
