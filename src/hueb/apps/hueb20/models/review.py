from django.contrib.auth.models import User
from django.db import models
from hueb.apps.hueb20.models import (
    Archive,
    Comment,
    Country,
    CulturalCircle,
    DdcGerman,
    Document,
    Filing,
    Person,
)
from hueb.apps.hueb20.models.utils import HUEB20, HUEB_APPLICATIONS
from simple_history.models import HistoricalRecords

NOT_REVIEWED = "NOT_REVIEWED"
CHANGES_NECESSARY = "CHANGES_NECESSARY"
OK = "OK"

REVIEW_STATES = [
    (NOT_REVIEWED, "Not reviewed"),
    (CHANGES_NECESSARY, "Changes necessary"),
    (OK, "Successfully Reviewed"),
]


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=20, choices=REVIEW_STATES, default=NOT_REVIEWED)
    note = models.ForeignKey(
        Comment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="review_comment",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="review_user",
    )

    cultural_circle = models.ForeignKey(
        CulturalCircle,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_culturalcircle",
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_document",
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_person",
    )
    archive = models.ForeignKey(
        Archive,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_archive",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_country",
    )
    filing = models.ForeignKey(
        Filing,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_filing",
    )
    ddc_german = models.ForeignKey(
        DdcGerman,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_ddc",
    )
    app = models.CharField(max_length=6, choices=HUEB_APPLICATIONS, default=HUEB20)
    history = HistoricalRecords()

    def __str__(self):
        return self.state
