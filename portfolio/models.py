from django.db import models
from django.template.defaultfilters import slugify

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

# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
def get_image_filename(instance, filename):
    title=instance.portfolio_item.title
    slug = slugify(title)
    return "portfolio_item_images/%s-%s" % (slug, filename)

class Images(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

    def __str__(self):
        return self.portfolio_item

class Accomplishment(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, default=None, on_delete=models.CASCADE)
    description=models.TextField()
