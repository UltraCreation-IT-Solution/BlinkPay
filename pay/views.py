from django.shortcuts import render
from rest_framework.views import APIView
from .models import Payment_details
from rest_framework.response import Response
from .serializers import *
# Create your views here.
class Show_Payment(APIView):
    def get(self,request):
        data = Payment_details.objects.all()
        serialize = PaymentSerializer(data,many = True)
        return Response(serialize.data)
