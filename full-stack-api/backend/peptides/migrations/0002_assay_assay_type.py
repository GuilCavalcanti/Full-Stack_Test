# Generated by Django 3.2.6 on 2021-09-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peptides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='assay_type',
            field=models.CharField(choices=[('WT', 'Wet'), ('DY', 'Dry')], default='WT', max_length=3),
        ),
    ]
