from django.urls import path

from . import views

app_name='portfolio'
urlpatterns=[
    path(r'', views.home, name='home'),
    path(r'portfolio', views.portfolio_category_list, name='portfolio_filter'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
