from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('logo-list/', views.logoList, name="logo-list"),
	path('logo-detail/<str:pk>/', views.logoDetail, name="logo-detail"),
	path('logo-create/', views.logoCreate, name="logo-create"),

	path('logo-update/<str:pk>/', views.logoUpdate, name="logo-update"),
	path('logo-delete/<str:pk>/', views.logoDelete, name="logo-delete"),
]