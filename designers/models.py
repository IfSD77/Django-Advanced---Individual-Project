from django.db import models

class Designer(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name='Full name'
    )
    profession = models.CharField(
        max_length=100,
        verbose_name='Profession / Specialty',
        help_text='e.g. Architect, Engineer, Technician, Surveyor'
    )
    initials = models.CharField(
        max_length=4,
        blank=True,
        verbose_name='Initials (for drawings/signatures)'
    )
    short_bio = models.TextField(
        blank=True,
        verbose_name='Short bio / Experience'
    )

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        if self.initials:
            return f"{self.full_name} ({self.initials})"
        return self.full_name

