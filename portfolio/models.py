from django.db import models

class PortfolioItem(models.Model):

    # TODO : Add tagging app
    # TODO : Add role model with foreign keys
    # TODO : Add software-tools model with foreign keys
    # TODO : Add picture model with foreign keys
    # TODO : Add category model with foreign keys

    title = models.CharField(max_length=200)
    started_date = models.DateField()
    ended_date = models.DateField()
    description = models.TextField()
