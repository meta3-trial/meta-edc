# Generated by Django 3.0.6 on 2020-05-16 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meta_subject", "0036_auto_20200517_0150"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalmissedvisit",
            old_name="contact_attempts_made",
            new_name="contact_attempts_count",
        ),
        migrations.RenameField(
            model_name="missedvisit",
            old_name="contact_attempts_made",
            new_name="contact_attempts_count",
        ),
    ]
