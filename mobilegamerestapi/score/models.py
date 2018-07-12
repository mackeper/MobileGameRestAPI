from django.db import models
from user.models import User


class Score(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('date',)

    # def save(self, *args, **kwargs):
    #    super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + str(self.score)

    def __unicode__(self):
        return self.name
