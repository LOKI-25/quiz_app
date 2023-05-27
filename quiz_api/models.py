from django.db import models

class Quiz(models.Model):
    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished')
    )

    question = models.CharField(max_length=255)
    options = models.JSONField(null=True, blank=True)
    right_answer = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
