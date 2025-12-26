from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path("products/", views.product_list, name="product-list"),
    path("products/create/", views.product_create, name="product-create"),
]
