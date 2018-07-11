from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)