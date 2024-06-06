from django.urls import path
from . import views

urlpatterns = [
    path('api/locations', views.LocationsList.as_view(), name='locations_list'), # api/locations will be routed to the LocationsList view for handling
    path('api/locations/<int:pk>', views.LocationsDetail.as_view(), name='locations_detail'), # api/locations will be routed to the LocationsDetail view for handling
]