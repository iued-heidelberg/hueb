# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION, ContentType
from hueb.apps.hueb20.models.document import Document, DocumentRelationship
from datetime import datetime, timedelta


class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    @receiver(post_save, sender=User)
    def create_user_history(sender, instance, created, **kwargs):
        if created:
            UserHistory.objects.create(user=instance)

    def get_additions(self):
        return (
            LogEntry.objects.filter(user_id=self.user.id)
            .filter(action_flag=ADDITION)
            .all()
        )

    def model_additions(self, model):
        ctype = ContentType.objects.get(app_label="hueb20", model=model)
        return self.get_additions().filter(content_type=ctype).all()

    def recent_additions(self, additions):
        now = datetime.now()
        this_month = len(
            additions.filter(action_time__month=now.month).filter(
                action_time__year=now.year
            )
        )
        then = now.replace(day=1)
        then = then - timedelta(days=1)
        last_month = len(
            additions.filter(action_time__month=then.month).filter(
                action_time__year=then.year
            )
        )
        return f"This Month:\t{this_month}\nLast Month:\t{last_month}"

    def total_addition_count(self):
        return len(self.get_additions())

    def recent_document_additions(self):
        return self.recent_additions(self.model_additions("document"))

    def document_addition_count(self):
        return len(self.model_additions("document"))

    def recent_person_additions(self):
        return self.recent_additions(self.model_additions("person"))

    def person_addition_count(self):
        return len(self.model_additions("person"))

    class Meta:
        verbose_name = "Entries per User"
        verbose_name_plural = "Entries per User"

    """
    def get_additions(self):
        additions = []
        logs = LogEntry.objects.filter(user_id=self.user.id).filter(action_flag=ADDITION).filter().all()
        for log in logs:
            ReviewModelId = ContentType.objects.get(model='reviewable')
    """
