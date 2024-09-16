from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    # Choices for Major
    COMPUTER_SCIENCE = 'CS'
    MATHEMATICS = 'MATH'
    BIOLOGY = 'BIO'
    CHEMISTRY = 'CHEM'
    PHYSICS = 'PHY'
    MAJOR_CHOICES = [
        (COMPUTER_SCIENCE, 'Computer Science'),
        (MATHEMATICS, 'Mathematics'),
        (BIOLOGY, 'Biology'),
        (CHEMISTRY, 'Chemistry'),
        (PHYSICS, 'Physics'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(
        help_text='Enter age in years',
        validators=[MinValueValidator(1), MaxValueValidator(90)]
    )
    address = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)
    major = models.CharField(
        max_length=4,
        choices=MAJOR_CHOICES,
        default=COMPUTER_SCIENCE,
    )
    slug = models.SlugField(max_length=100, unique=True)

    def create_unique_slug(self):
        import time

        slug = slugify(self.name + ' ' + str(time.time()))
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
