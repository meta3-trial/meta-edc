# Generated by Django 3.0.6 on 2020-05-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_lists", "0005_auto_20191104_0930"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="arvregimens",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "ARV Regimens",
                "verbose_name_plural": "ARV Regimens",
            },
        ),
        migrations.AlterModelOptions(
            name="baselinesymptoms",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Baseline Symptoms",
                "verbose_name_plural": "Baseline Symptoms",
            },
        ),
        migrations.AlterModelOptions(
            name="diabetessymptoms",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Diabetes Symptoms",
                "verbose_name_plural": "Diabetes Symptoms",
            },
        ),
        migrations.AlterModelOptions(
            name="hypertensionmedications",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Hypertension Medications",
                "verbose_name_plural": "Hypertension Medications",
            },
        ),
        migrations.AlterModelOptions(
            name="nonadherencereasons",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Non-Adherence Reasons",
                "verbose_name_plural": "Non-Adherence Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="offstudyreasons",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Offstudy Reasons",
                "verbose_name_plural": "Offstudy Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="oiprophylaxis",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "OI Prophylaxis",
                "verbose_name_plural": "OI Prophylaxis",
            },
        ),
        migrations.AlterModelOptions(
            name="symptoms",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Symptoms",
                "verbose_name_plural": "Symptoms",
            },
        ),
    ]