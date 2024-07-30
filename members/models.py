from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GRADE_CHOICES = [
        ('O', 'Other'),
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
        ('12', '12th Grade'),
        ('F', 'College Freshman'),
        ('S', 'College Sophomore'),
        ('J', 'College Junior'),
        ('S', 'College Senior'),
    ]
    
    MENTOR_MENTEE_CHOICES = [
        ('mentor', 'Mentor'),
        ('mentee', 'Mentee'),
    ]

    NEED_MERIT_CHOICES = [
        ('N', 'Need-based aid'),
        ('M', 'Merit-based aid'),
    ]
    
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True)
    major = models.TextField(max_length=20, blank=True)
    financial_situation = models.CharField(max_length=3, choices=NEED_MERIT_CHOICES, blank=True)
    mentor_or_mentee = models.CharField(max_length=6, choices=MENTOR_MENTEE_CHOICES, blank=True)
    matched = models.BooleanField(default=False)  # True if matched, False if unmatched

    def __str__(self):
        return self.username

