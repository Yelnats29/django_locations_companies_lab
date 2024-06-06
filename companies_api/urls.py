from django.urls import path
from . import views

urlpatterns = [
    path('api/companies', views.CompaniesList.as_view(), name='companies_list'), # api/companies will be routed to the CompaniesList view for handling
    path('api/companies/<int:pk>', views.CompaniesDetail.as_view(), name='companies_detail'), # api/companies will be routed to the CompaniesDetail view for handling
]