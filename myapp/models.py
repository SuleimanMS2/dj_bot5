from django.db import models


class Test(models.Model):
    question = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)

    def __str__(self):
        return self.question




