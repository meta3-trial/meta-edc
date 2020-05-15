# Generated by Django 3.0.6 on 2020-05-15 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0031_auto_20200422_2039"),
    ]

    operations = [
        migrations.RemoveField(model_name="historicalcoronakap", name="history_user",),
        migrations.RemoveField(model_name="historicalcoronakap", name="site",),
        migrations.RemoveField(model_name="historicalcoronakap", name="subject_visit",),
        migrations.AlterModelOptions(
            name="bloodresultsfbc",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: FBC",
                "verbose_name_plural": "Blood Results: FBC",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultsglu",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: Glucose",
                "verbose_name_plural": "Blood Results: Glucose",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultshba1c",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: HbA1c",
                "verbose_name_plural": "Blood Results: HbA1c",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultslft",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: LFT",
                "verbose_name_plural": "Blood Results: LFT",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultslipid",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: Lipids",
                "verbose_name_plural": "Blood Results: Lipids",
            },
        ),
        migrations.AlterModelOptions(
            name="bloodresultsrft",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Blood Result: RFT",
                "verbose_name_plural": "Blood Results: RFT",
            },
        ),
        migrations.AlterModelOptions(
            name="complications",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Presence of Complications",
                "verbose_name_plural": "Presence of Complications",
            },
        ),
        migrations.AlterModelOptions(
            name="followup",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Clinic follow up: Examination",
                "verbose_name_plural": "Clinic follow up: Examination",
            },
        ),
        migrations.AlterModelOptions(
            name="followupvitals",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Clinic follow up: Vitals",
                "verbose_name_plural": "Clinic follow ups: Vitals",
            },
        ),
        migrations.AlterModelOptions(
            name="healtheconomics",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Health Economics",
                "verbose_name_plural": "Health Economics",
            },
        ),
        migrations.AlterModelOptions(
            name="malariatest",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Malaria Test",
            },
        ),
        migrations.AlterModelOptions(
            name="medicationadherence",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Medication Adherence",
                "verbose_name_plural": "Medication Adherence",
            },
        ),
        migrations.AlterModelOptions(
            name="patienthistory",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Patient History",
                "verbose_name_plural": "Patient History",
            },
        ),
        migrations.AlterModelOptions(
            name="physicalexam",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Physical Exam",
                "verbose_name_plural": "Physical Exams",
            },
        ),
        migrations.AlterModelOptions(
            name="urinedipsticktest",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Urine Dipstick Test",
            },
        ),
        migrations.DeleteModel(name="CoronaKap",),
        migrations.DeleteModel(name="HistoricalCoronaKap",),
    ]