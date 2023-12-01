from django.urls import path, include

urlpatterns = [
    path('pos_system/products/', include('pos_test.urls.product')),
]
