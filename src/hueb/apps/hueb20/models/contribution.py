import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.document import Document
from hueb.apps.hueb20.models.person import Person
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from hueb.apps.tenants.models import TENANT_APPS, TenantAwareModel


class Contribution(Reviewable, TenantAwareModel):
    PUBLISHER = "PUBLISHER"
    WRITER = "WRITER"
    OTHER = "OTHER"

    CONTRIBUTION_TYPES = [
        (PUBLISHER, "Publisher"),
        (WRITER, "Writer"),
        (OTHER, "Other"),
    ]

    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, null=True, blank=True
    )
    contribution_type = models.CharField(
        max_length=20, choices=CONTRIBUTION_TYPES, blank=True, null=True
    )

    originalAuthor_ref = models.OneToOneField(
        Legacy.OriginalNewAuthorNew, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    translationTranslator_ref = models.OneToOneField(
        Legacy.TranslationNewTranslatorNew,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    app = models.CharField(
        max_length=6, choices=HUEB_APPLICATIONS + TENANT_APPS, default=HUEB20
    )

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            super().mark_reviewed(updated=updated)
            self.person.mark_reviewed(updated)
            super(Document, self.document).mark_reviewed(updated)

    def __str__(self):
        person = str(self.person)
        document = str(self.document)
        contribution = self.get_contribution_type_display()
        return '"{}" is "{}" for "{}"'.format(person, contribution, document)

    def linked_name(self):
        url = reverse(
            "admin:hueb20_contribution_change",
            args=[self.id],
        )
        link = '<a href="%s">Contribution: %s</a>' % (url, str(self))
        return link
