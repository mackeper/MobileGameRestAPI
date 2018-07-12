from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='score', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)

    def save(self, *args, **kwargs):
        super(Score, self).save(*args, **kwargs)