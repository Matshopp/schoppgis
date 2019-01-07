from django.db import models


# TODO : Add tagging app
# TODO : Add role model with foreign keys
# TODO : Add software-tools model with foreign keys
# TODO : Add picture model with foreign keys
# TODO : Add category model with foreign keys

class Role(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class IndustryArea(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class SoftwareAndTool(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Employer(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class PortfolioItem(models.Model):

    title = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    started_date = models.DateField()
    ended_date = models.DateField()
    description = models.TextField()
    main_categories = models.ManyToManyField(MainCategory, blank=True)
    software_tools = models.ManyToManyField(SoftwareAndTool, blank=True)
    industry_area = models.ForeignKey(IndustryArea, blank=True, null=True, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, blank=True)
    employer = models.ForeignKey(Employer, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
