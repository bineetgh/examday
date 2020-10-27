from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    hint1 = models.CharField(max_length=255)
    hint2 = models.CharField(max_length=255)
    hint3 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
    ])
    solution = models.TextField()
    level = models.IntegerField(default='3', choices=[
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5')
    ])


