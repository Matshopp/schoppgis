from django.shortcuts import render
from .models import PortfolioItem, PortfolioCategory, PortfolioPosition, PortfolioIndustry, PortfolioSoftwareTool, PortfolioEmployer

def portfolio_category_list(request):
    portfolio_categories = dict()
    portfolio_categories['positions']=PortfolioPosition.objects.all()
    portfolio_categories['categories'] = PortfolioCategory.objects.all()
    portfolio_categories['industries'] = PortfolioIndustry.objects.all()
    portfolio_categories['software_tools'] = PortfolioSoftwareTool.objects.all()
    portfolio_categories['employers'] = PortfolioEmployer.objects.all()
    return render(request, 'portfolio/portfolio_category_list.html', {'portfolio_categories':portfolio_categories})

def portfolio_item_list(request, position_title):
    portfolio_items = PortfolioItem.objects.filter(position__title=position_title)
    return render(request, 'portfolio/portfolio_item_list.html', {'portfolio_items':portfolio_items})
