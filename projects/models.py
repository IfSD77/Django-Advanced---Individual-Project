from django.db import models
from django.utils.text import slugify


class ConstructionType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Construction Type"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Construction Type"
        verbose_name_plural = "Construction Types"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Project Name'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="Slug (for URL)"
    )
    construction_type = models.ForeignKey(
        ConstructionType,
        on_delete=models.PROTECT,
        verbose_name='Construction Type',
        related_name='projects'
    )
    location = models.CharField(
        max_length=100,
        verbose_name='Location'
    )
    postcode = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Postcode',
    )
    built_in = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Built In",
        help_text="Year when the project was completed"
    )
    contract_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Contract Value (£)",
        help_text="Approximate contract value in GBP"
    )
    contract_value_confidential = models.BooleanField(
        default=False,
        verbose_name="Contract Value is Confidential"
    )
    description = models.TextField(blank=True, verbose_name="Project Description")
    image = models.ImageField(
        upload_to='projects/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name="Main Project Image"
    )

    class Meta:
        ordering = ['-built_in', 'name']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)

        if self.postcode:
            self.postcode = self.postcode.upper().strip()

        super().save(*args, **kwargs)

    def __str__(self):
        year_part = f" ({self.built_in})" if self.built_in else ""
        return f"{self.name}{year_part}"

    def get_contract_value_short(self):
        if self.contract_value_confidential:
            return "Confidential"
        if self.contract_value is None or self.contract_value == 0:
            return "N/A"

        value = float(self.contract_value)
        if value >= 1_000_000:
            return f"£{value / 1_000_000:.1f}m"
        elif value >= 1_000:
            return f"£{value / 1_000:,.0f}k"
        else:
            return f"£{value:,.0f}"