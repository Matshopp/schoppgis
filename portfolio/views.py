from django.shortcuts import render
from .models import PortfolioItem, MainCategory, Role, IndustryArea, SoftwareAndTool, Employer
from .filters import PortfolioItemFilter

"""
def search(request):
    user_list = Role.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'portfolio/position_list.html', {'filter':user_filter})
"""
def portfolio_category_list(request):
    portfolio_item_list = PortfolioItem.objects.all()
    portfolio_filter = PortfolioItemFilter(request.GET, queryset=portfolio_item_list)
    has_filter = any(field in request.GET for field in set(portfolio_filter.get_fields()))
    return render(request, 'portfolio/portfolio_category_list.html', {'portfolio_filter':portfolio_filter, 'has_filter': has_filter})

def portfolio_item_list(request, role_name):
    #portfolio_items = PortfolioItem.objects.filter(roles__name=role_name)
    portfolio_items = PortfolioItem.objects.all()
    user_filter = PortfolioItemFilter(request.GET, queryset=portfolio_items)
    #return render(request, 'portfolio/portfolio_item_list.html', {'portfolio_items':portfolio_items})
    return render(request, 'portfolio/portfolio_item_list.html', {'filter': user_filter})
