from django.urls import path
from . import views

app_name = 'text'
urlpatterns = [
                path('housingdata', views.HousingDataCreateView,
                            name='housingdata'),
                path('', views.TextModelsView, name='text'),
                path('sendhousingdata', views.HousingDataCreateView, name='sendhousingdata'),
]