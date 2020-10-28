from django.db import models

# Create your models here.


class TestSeries(models.Model):
    title = models.CharField(max_length=100)
    exam = models.TextField(choices=[
        ('CTET', 'CTET'), 
        ('Primary', 'Primary'), 
        ('Secondary', 'Secondary'), 
        ('IIT-JEE', 'IIT-JEE'), 
        ('10th', '10th'), 
        ('12th', '12th'), 
        ('NEET', 'NEET')])
    year = models.IntegerField()

    def __str__(self):
        return self.title

class TestSet(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(TestSeries, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(default='3', choices=[
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5')
    ])

    def __str__(self):
        return self.name
    


class Question(models.Model):
    title = models.CharField(max_length=255)
    test_set = models.ForeignKey(TestSet, on_delete=models.SET_NULL, null=True)
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

    def __str__(self):
        return self.title
