from django.urls import path

from . import views

app_name='portfolio'
urlpatterns=[
    path(r'', views.portfolio_category_list, name='portfolio_category_list'),
    path(r'<position_title>/', views.portfolio_item_list, name='portfolio_item_list'),

]
