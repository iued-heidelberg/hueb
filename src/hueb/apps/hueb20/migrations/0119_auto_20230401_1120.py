# Generated by Django 3.2.5 on 2023-04-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0118_auto_20230226_1754"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archive",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="contribution",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="culturalcircle",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="ddcgerman",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                    ("GUEBFR", "GÜB-FR"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="documentrelationship",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="filing",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalarchive",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomment",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcontribution",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcountry",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalculturalcircle",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalddcgerman",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldocument",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                    ("GUEBFR", "GÜB-FR"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldocumentrelationship",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalfiling",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicallanguage",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="historicalperson",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="app",
            field=models.CharField(
                choices=[
                    ("LATEIN", "SÜB-Lat"),
                    ("LIDOS", "DFÜ-FR"),
                    ("LEGACY", "SÜB-Rom"),
                    ("HUEB20", "HÜB-EN-NL"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
    ]
