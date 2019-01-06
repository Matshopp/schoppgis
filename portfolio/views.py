from django.shortcuts import render
from .models import PortfolioItem, MainCategory, Role, IndustryArea, SoftwareAndTool, Employer
from .filters import UserFilter

"""
def search(request):
    user_list = Role.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'portfolio/position_list.html', {'filter':user_filter})
"""
def portfolio_category_list(request):
    portfolio_categories = dict()
    portfolio_categories['roles']=Role.objects.all()
    portfolio_categories['categories'] = MainCategory.objects.all()
    portfolio_categories['industries'] = IndustryArea.objects.all()
    portfolio_categories['software_tools'] = SoftwareAndTool.objects.all()
    portfolio_categories['employers'] = Employer.objects.all()
    return render(request, 'portfolio/portfolio_category_list.html', {'portfolio_categories':portfolio_categories})

def portfolio_item_list(request, position_title):
    portfolio_items = PortfolioItem.objects.filter(position__title=position_title)
    return render(request, 'portfolio/portfolio_item_list.html', {'portfolio_items':portfolio_items})
