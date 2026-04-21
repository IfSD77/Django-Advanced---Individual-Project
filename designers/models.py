from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Designer(models.Model):
    full_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=100, choices=[
        ('architect', 'Architect'),
        ('structural_engineer', 'Structural Engineer'),
        ('mechanical_engineer', 'Mechanical Engineer'),
        ('electrical_engineer', 'Electrical Engineer'),
        ('interior_designer', 'Interior Designer'),
    ])
    short_bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('designer_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
