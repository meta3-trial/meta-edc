# Generated by Django 3.0.4 on 2020-04-20 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_subject', '0026_auto_20200420_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronakap',
            name='diabetic_on_meds',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='Are you taking medications to control your <u>diabetes</u>?'),
        ),
        migrations.AlterField(
            model_name='coronakap',
            name='diabetic_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first learn you had <u>diabetes</u>?'),
        ),
        migrations.AlterField(
            model_name='coronakap',
            name='hiv_pos_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first test positive?'),
        ),
        migrations.AlterField(
            model_name='coronakap',
            name='hypertensive_on_meds',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='Are you taking medications to control your <u>hypertension</u>?'),
        ),
        migrations.AlterField(
            model_name='coronakap',
            name='hypertensive_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first learn you had <u>hypertension</u>?'),
        ),
        migrations.AlterField(
            model_name='historicalcoronakap',
            name='diabetic_on_meds',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='Are you taking medications to control your <u>diabetes</u>?'),
        ),
        migrations.AlterField(
            model_name='historicalcoronakap',
            name='diabetic_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first learn you had <u>diabetes</u>?'),
        ),
        migrations.AlterField(
            model_name='historicalcoronakap',
            name='hiv_pos_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first test positive?'),
        ),
        migrations.AlterField(
            model_name='historicalcoronakap',
            name='hypertensive_on_meds',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=25, verbose_name='Are you taking medications to control your <u>hypertension</u>?'),
        ),
        migrations.AlterField(
            model_name='historicalcoronakap',
            name='hypertensive_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MinValueValidator(2020)], verbose_name='What year did you first learn you had <u>hypertension</u>?'),
        ),
    ]
