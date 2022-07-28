from django.urls import path

from products.views import ProductView, ProductIdView



urlpatterns = [
    path("products/", ProductView.as_view()),
    path("peoducts/<str:product_uuid>", ProductIdView.as_view()
    )

]