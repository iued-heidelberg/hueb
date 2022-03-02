import hueb.apps.hueb_legacy_latein.models as Legacy
import hueb.apps.hueb_legacy.models as LegacyLegacy
from django.db import models
from django.urls import reverse
from hueb.apps.hueb20.models.archive import Archive
from hueb.apps.hueb20.models.document import Document
from hueb.apps.hueb20.models.reviewable import Reviewable
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS


class Filing(Reviewable):
    id = models.BigAutoField(primary_key=True)
    archive = models.ForeignKey(
        Archive, on_delete=models.CASCADE, null=True, blank=True
    )
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, null=True, blank=True
    )
    signatur = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    locAssign_ref = models.ForeignKey(
        Legacy.LocAssign, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    locAssign_legacy_ref = models.ForeignKey(
        LegacyLegacy.LocAssign,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="hueb20_filing_set",
    )

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            super().mark_reviewed(updated=updated)

            self.archive.mark_reviewed(updated)
            self.document.mark_reviewed(updated)

    def __str__(self):
        document = str(self.document)
        archive = str(self.archive)
        return '"{}" archived in "{}"'.format(document, archive)

    def linked_name(self):
        url = reverse(
            "admin:hueb20_filing_change",
            args=[self.id],
        )
        link = '<a href="%s">Filing: %s</a>' % (url, str(self))
        return link
