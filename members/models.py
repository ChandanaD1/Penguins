from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GRADE_CHOICES = [
        ('', 'Select'),
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
        ('12', '12th Grade'),
        ('F', 'College Freshman'),
        ('S', 'College Sophomore'),
        ('J', 'College Junior'),
        ('S', 'College Senior'),
    ]
    
    STATUS_CHOICES = [
        ('', 'Select'),
        ('mentor', 'Mentor'),
        ('mentee', 'Mentee'),
    ]

    NEED_MERIT_CHOICES = [
        ('', 'Select'),
        ('N', 'Need-based aid'),
        ('M', 'Merit-based aid')
    ]
    
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True)
    major = models.TextField(max_length=50, blank=True)
    college = models.TextField(max_length=50, blank=True)
    financial_situation = models.CharField(max_length=3, choices=NEED_MERIT_CHOICES, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, blank=False)
    matched = models.BooleanField(default=False)  # True if matched, False if unmatched

