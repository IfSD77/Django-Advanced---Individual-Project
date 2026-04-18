from django.db import models


class Participation(models.Model):
    ROLE_CHOICES = [
        ('architect', 'Architect'),
        ('lead_architect', 'Lead Architect'),
        ('architectural_designer', 'Architectural Designer'),
        ('structural_engineer', 'Structural Engineer'),
        ('senior_structural_engineer', 'Senior Structural Engineer'),
        ('structural_designer', 'Structural Designer'),
        ('technical_lead', 'Technical Lead'),
        ('structural_consultant', 'Structural Consultant'),
        ('other', 'Other'),
    ]

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='participations'
    )
    designer = models.ForeignKey(
        'designers.Designer',
        on_delete=models.PROTECT,
        related_name='participations'
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        verbose_name="Role in the project"
    )
    contribution = models.TextField(
        blank=True,
        verbose_name="Contribution / Notes"
    )

    class Meta:
        unique_together = [['project', 'designer']]
        ordering = ['project', 'role']
        verbose_name = "Team Participation"
        verbose_name_plural = "Team Participations"

    def __str__(self):
        return f"{self.designer} – {self.get_role_display()} in {self.project}"