# challenges/models.py
from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    user_code = models.TextField()
    result = models.TextField()

    def __str__(self):
        return f"Submission for {self.challenge.title}"

class TestCase(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()