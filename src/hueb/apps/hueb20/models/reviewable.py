from django.db import models
from hueb.apps.hueb20.models.utils import NOT_REVIEWED, REVIEW_STATES


class Reviewable(models.Model):
    def __init__(self, review_state=NOT_REVIEWED):
        if review_state in REVIEW_STATES:
            self.review = review_state

    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=20, choices=REVIEW_STATES, default=NOT_REVIEWED)
    reviewed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True
