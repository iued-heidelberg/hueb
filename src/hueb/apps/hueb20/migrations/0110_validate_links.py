from multiprocessing import Pool

import requests
import timeout_decorator
from django.db import migrations


@timeout_decorator.timeout(
    5, timeout_exception=TimeoutError, exception_message="too long response time"
)
def check_validity(link):
    rq = requests.get(link)
    if rq.status_code == 200:  # OK success status
        return True
    else:
        return False


def process_doc(link_index):
    link, index = link_index
    if index % 100 == 0:
        print(index)
    try:
        return check_validity(link)
    except TimeoutError:
        print("Timeout Error")
        return False
    except Exception:
        return False


def validate_links(apps, schema_editor):

    Filing = apps.get_model("hueb20", "Filing")
    filings_no_links = (
        Filing.objects.filter(archive__name="Online-Version")
        .filter(link__isnull=True)
        .all()
    )
    for filing in filings_no_links:
        filing.link_status = False
        filing.save()

    filings = (
        Filing.objects.filter(archive__name="Online-Version")
        .filter(link__isnull=False)
        .all()
    )
    total = len(filings)
    indices = range(len(filings))
    print("Total: ", total)
    with Pool(8) as p:
        valids = p.map(process_doc, zip([filing.link for filing in filings], indices))

    for filing, valid in zip(filings, valids):
        filing.link_status = valid
        filing.save()


def clean_link_status(apps, schema_editor):

    Filing = apps.get_model("hueb20", "Filing")
    filings = Filing.objects.filter(archive__name="Online-Version").all()
    for filing in filings:
        filing.link_status = None
        filing.save()


class Migration(migrations.Migration):

    dependencies = [
        ("hueb20", "0109_auto_20221022_1049"),
    ]

    operations = [
        migrations.RunPython(validate_links, clean_link_status),
    ]
