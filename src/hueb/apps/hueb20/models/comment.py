from django.db import models
from django.template.defaultfilters import escape
from hueb.apps.hueb20.models.culturalCircle import CulturalCircle
from hueb.apps.hueb20.models.document import Document
from hueb.apps.hueb20.models.person import Person
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from hueb.apps.tenants.models import TENANT_APPS, TenantAwareModel
from simple_history.models import HistoricalRecords


class Comment(TenantAwareModel):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    external = models.BooleanField(
        default=False,
        help_text="External comments will be displayed on the public website.",
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="person_comment",
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="document_comment",
    )
    cultural_circle = models.ForeignKey(
        CulturalCircle,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cultural_circle_comment",
    )
    app = models.CharField(
        max_length=6, choices=HUEB_APPLICATIONS + TENANT_APPS, default=HUEB20
    )
    history = HistoricalRecords()

    def __str__(self):
        if self.text is None:
            return " "
        return escape(self.text)
