from django.contrib import admin
from .models import PortfolioItem, MainCategory, SoftwareAndTool, Role, IndustryArea, Employer

admin.site.register(PortfolioItem)
admin.site.register(MainCategory)
admin.site.register(SoftwareAndTool)
admin.site.register(Role)
admin.site.register(IndustryArea)
admin.site.register(Employer)

# Register your models here.
