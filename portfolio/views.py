from django.shortcuts import render
from .models import PortfolioItem
from .filters import PortfolioItemFilter
from django.views import generic

def home(request):
    return render(request, 'portfolio/index.html')

class DetailView(generic.DetailView):
    model = PortfolioItem
    template_name = 'portfolio/detail.html'

def portfolio_category_list(request):
    portfolio_item_list = PortfolioItem.objects.order_by('-started_date')
    portfolio_filter = PortfolioItemFilter(request.GET, queryset=portfolio_item_list)
    has_filter = any(field in request.GET for field in set(portfolio_filter.get_fields()))
    return render(request, 'portfolio/filter.html', {'portfolio_filter':portfolio_filter, 'has_filter': has_filter})
