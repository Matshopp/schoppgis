from django.contrib.auth.models import User
from .models import PortfolioItem
import django_filters

class PortfolioItemFilter(django_filters.FilterSet):

    class Meta:
        model = PortfolioItem
        fields=['industry_area','software_tools','main_categories', 'employer']