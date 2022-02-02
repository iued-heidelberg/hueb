from django.db import migrations, models


def create_user_histories(apps, schema_editor):
    UserModel = apps.get_model("auth", "User")
    UserHistory = apps.get_model("user_history", "UserHistory")
    users = UserModel.objects.all()

    for u in users:
        uh = UserHistory()
        uh.user = u
        uh.save()


def uncreate_user_histories(apps, schema_editor):
    UH = apps.get_model("user_history", "UserHistory")
    uh = UH.objects.all()
    uh.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("user_history", "0002_alter_userhistory_options"),
    ]

    operations = [migrations.RunPython(create_user_histories, uncreate_user_histories)]
