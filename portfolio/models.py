from django.db import models


# TODO : Add tagging app
# TODO : Add role model with foreign keys
# TODO : Add software-tools model with foreign keys
# TODO : Add picture model with foreign keys
# TODO : Add category model with foreign keys

class PortfolioPosition(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class PortfolioIndustry(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class PortfolioSoftwareTool(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class PortfolioCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class PortfolioEmployer(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class PortfolioItem(models.Model):

    title = models.CharField(max_length=200)
    started_date = models.DateField()
    ended_date = models.DateField()
    description = models.TextField()
    categories = models.ManyToManyField(PortfolioCategory, blank=True)
    software_tools = models.ManyToManyField(PortfolioSoftwareTool, blank=True)
    industry = models.ForeignKey(PortfolioIndustry, blank=True, null=True, on_delete=models.CASCADE)
    position = models.ManyToManyField(PortfolioPosition, blank=True)
    employer = models.ForeignKey(PortfolioEmployer, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
