# flake8: noqa
import csv
import re

from django.db import migrations
from psycopg2.extras import NumericRange


def edit_comments(apps, schema_editor):
    
    #edit the comments from HUES that have the numbers up to VD16/17/18 to remove the text after the VD16/17/18
    HUES = "HUES"   
    Hues_comment = apps.get_model("hueb20", "Comment")
    comments = Hues_comment.objects.filter(tenant__app=HUES).exclude(text__icontains="VD").all()
    for comment in comments:
        comment.delete()
        
    
def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("hueb20", "0130_hues_import_2_correct")]
    operations = [migrations.RunPython(edit_comments, reverse)]