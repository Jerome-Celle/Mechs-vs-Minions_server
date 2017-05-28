from django.db import models

class Minion(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    posX = models.IntegerField()
    posY = models.IntegerField()

    class Meta:
        ordering = ('created',)

class CaseHuile(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    posX = models.IntegerField()
    posY = models.IntegerField()

    class Meta:
        ordering = ('created',)