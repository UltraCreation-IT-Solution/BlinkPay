from django.urls import path
from .views import *
urlpatterns = [
    path('',Show_Payment.as_view(),name = "Payment_data" ),
    path('auto/<str:card_id>/',automation,name = "automation")
]