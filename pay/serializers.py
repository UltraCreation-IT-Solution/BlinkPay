from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import *

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment_details
        fields = "__all__"