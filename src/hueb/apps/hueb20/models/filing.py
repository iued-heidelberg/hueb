import hueb.apps.hueb_legacy_latein.models as Legacy
from django.db import models
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
