from django.db import models
from django.contrib.auth.models import User


class Peptide(models.Model):
    sequence = models.CharField(max_length=30)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Assay(models.Model):
    name = models.CharField(max_length=20)
    operator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assays'
    )
    peptides = models.ManyToManyField(
        Peptide,
        related_name='assays',
        blank=True
    )
    # Excercise 3 ADD-CODE-HERE
    WET = 'WT'
    DRY = 'DY'
    ASSAY_TYPES = [
        (WET, 'Wet'),
        (DRY, 'Dry'),
    ]
    assay_type = models.CharField(
        max_length=3,
        choices=ASSAY_TYPES,
        default=ASSAY_TYPES[0][0]
    )

    def __str__(self):
        return self.name


