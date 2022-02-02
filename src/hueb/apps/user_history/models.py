# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION


class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    @receiver(post_save, sender=User)
    def create_user_history(sender, instance, created, **kwargs):
        if created:
            UserHistory.objects.create(user=instance)

    def addition_count(self):
        return len(
            LogEntry.objects.filter(user_id=self.user.id)
            .filter(action_flag=ADDITION)
            .all()
        )

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
