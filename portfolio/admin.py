from django.contrib import admin
from .models import PortfolioItem, PortfolioCategory, PortfolioSoftwareTool, PortfolioPosition, PortfolioIndustry, PortfolioEmployer

admin.site.register(PortfolioItem)
admin.site.register(PortfolioCategory)
admin.site.register(PortfolioSoftwareTool)
admin.site.register(PortfolioPosition)
admin.site.register(PortfolioIndustry)
admin.site.register(PortfolioEmployer)

# Register your models here.
