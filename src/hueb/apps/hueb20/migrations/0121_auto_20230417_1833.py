# Generated by Django 3.2.5 on 2023-04-17 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tenants", "0003_tenantuser"),
        ("hueb20", "0120_auto_20230406_0913"),
    ]

    operations = [
        migrations.AddField(
            model_name="contribution",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="country",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="culturalcircle",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="filing",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="historicalcontribution",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="historicalcountry",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="historicalculturalcircle",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="historicalfiling",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="historicalperson",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="tenants.tenant",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tenants.tenant",
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
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
                    ("GUEBFR", "GÜB-FR"),
                ],
                default="HUEB20",
                max_length=6,
            ),
        ),
    ]