# Generated by Django 3.0.6 on 2020-05-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0045_auto_20200530_1801"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="followupexamination", name="meta_subjec_subject_8cd273_idx",
        ),
        migrations.AlterField(
            model_name="followupexamination",
            name="admitted_hospital",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="If YES, were they admitted to hospital?",
            ),
        ),
        migrations.AlterField(
            model_name="followupexamination",
            name="attended_clinic_sae",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If YES, submit a <u>Serious Adverse Event</u> Form",
                max_length=25,
                verbose_name="Does the event constitute a <u>Serious Adverse Event</u>",
            ),
        ),
        migrations.AlterField(
            model_name="followupexamination",
            name="prescribed_medication",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Was the participant prescribed any other medication at this clinic or hospital visit?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfollowupexamination",
            name="admitted_hospital",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="If YES, were they admitted to hospital?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfollowupexamination",
            name="attended_clinic_sae",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                help_text="If YES, submit a <u>Serious Adverse Event</u> Form",
                max_length=25,
                verbose_name="Does the event constitute a <u>Serious Adverse Event</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfollowupexamination",
            name="prescribed_medication",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Was the participant prescribed any other medication at this clinic or hospital visit?",
            ),
        ),
        migrations.AddIndex(
            model_name="followupexamination",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="meta_subjec_subject_aad749_idx",
            ),
        ),
    ]