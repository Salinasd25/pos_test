from django.urls import path
from pos_test.apis import (
    ProductList,
)

urlpatterns = [
    path(
        '',
        ProductList.as_view(),
        name='products'
    ),
]
