from django.shortcuts import render
from django.forms import modelformset_factory
from .models import PortfolioItem, Images
from .filters import PortfolioItemFilter
from django.views import generic
from .forms import ImageForm, PortfolioItemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

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




def portfolio_item(request):

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=2)

    if request.method == 'Post':

        portfolioItemForm = PortfolioItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

        if portfolioItemForm.is_valid() and formset.is_valid():
            portfolio_item_form = portfolioItemForm.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    picture = Images(portfolio_item = portfolio_item_form, image=image)
                    picture.save()
            messages.success(request, "Image added")
            return HttpResponseRedirect("/")
        else:
            print(portfolioItemForm.errors, formset.errors)
    else:
        portfolioItemForm = PortfolioItemForm()
        formset = ImageFormSet(queryset=Images.objects.none())

    return render(request, 'index.html', {'postForm': portfolioItemForm, 'formset': formset})

# /*https://stackoverflow.com/questions/17591447/how-to-reload-current-page-without-losing-any-form-data*
# https://sixfeetup.com/blog/making-your-django-templates-ajax-y