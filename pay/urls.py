from django.urls import path
from .views import Show_Payment
urlpatterns = [
    path('',Show_Payment.as_view(),name = "Payment_data" )
]