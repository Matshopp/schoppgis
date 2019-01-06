from django.contrib.auth.models import User
from .models import PortfolioItem
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

"""
class PositionFilter(django_filters.FilterSet):
    class Meta:
        model = PortfolioPosition
        fields = ['title',]
        #model = PortfolioItem
        #fields = ['title', 'started_date', 'ended_date', 'description', 'categories', 'software_tools', 'industry', 'position', 'employer',]
"""