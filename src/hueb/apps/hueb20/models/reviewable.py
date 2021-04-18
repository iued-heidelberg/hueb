from django.db import models
from simple_history.models import HistoricalRecords


class Reviewable(models.Model):
    NOT_REVIEWED = "NOT_REVIEWED"
    CHANGES_NECESSARY = "CHANGES_NECESSARY"
    REREVIEW_NECESSARY = "REREVIEW_NECESSESARY"
    OK = "OK"

    REVIEW_STATES = [
        (NOT_REVIEWED, "Not reviewed"),
        (CHANGES_NECESSARY, "Changes necessary"),
        (REREVIEW_NECESSARY, "Rereview necessary"),
        (OK, "Successfully reviewed"),
    ]

    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=20, choices=REVIEW_STATES, default=NOT_REVIEWED)
    reviewed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    history = HistoricalRecords(inherit=True)

    def mark_reviewed(self, updated=[]):
        if self not in updated:
            self.state = self.OK
            self.save()
            updated.append(self)

        return

    def linked_name(self):
        return str(self)

    class Meta:
        abstract = True
        permissions = [("can_review", "Can review hueb entries")]
