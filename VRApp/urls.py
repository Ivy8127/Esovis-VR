from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),   
	path('shop/', views.shop, name="shop"),
	path('historical_sites/', views.historicalSites, name="historical_sites"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]