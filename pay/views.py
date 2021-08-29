from rest_framework.views import APIView
from .models import Payment_details
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
import webbrowser
import pyautogui
import time
import requests

# Create your views here.

class Show_Payment(APIView):
    def get(self,request):
        data = Payment_details.objects.all()
        serialize = PaymentSerializer(data,many = True)
        return Response(data = serialize.data,status = status.HTTP_200_OK)

@api_view(('GET',))
def automation(request,card_id):
    data = Payment_details.objects.get(card_id=card_id)
    serialize = PaymentSerializer(data)
    print(serialize.data)    
    url = "https://www.onlinesbi.com/sbicollect/icollecthome.htm?corpID=3802557"
    #url = "https://ultracreation.tech"
    web = webbrowser.open(url)
    response = requests.get(url)
    respones_time = response.elapsed.total_seconds()
    print(respones_time)
    pyautogui.press('f5')
    pyautogui.press('f5')
    pyautogui.press('f5')
    time.sleep(2)


    
    # Total Screen Size
    width, height= pyautogui.size()

    # For check box
    #Point(x=123, y=640)
    constant_for_width_checkbox = 11.10569105691057
    constant_for_heigth_checkbox = 1.2


    # For Proceed button
    constant_for_width_btn = 2.017725258493353
    constant_for_hight_btn = 1.114658925979681

    pyautogui.click(x = width/constant_for_width_checkbox ,y = height/constant_for_heigth_checkbox, clicks = 1, button = 'left')
    time.sleep(1)
    pyautogui.click(x = width/constant_for_width_btn ,y = height/constant_for_hight_btn, clicks = 1, button = 'left')
    
    constant_for_width_dropdown = 2.577358490566038
    constant_for_heigth_dropdown = 1.593360995850622
    time.sleep(2)
    pyautogui.click(x = width/constant_for_width_dropdown ,y = height/constant_for_heigth_dropdown, clicks = 1, button = 'left')
    pyautogui.press('down')
    pyautogui.press('enter')
    

    return Response(data = serialize.data,status = status.HTTP_200_OK)


    
    
    
    
    #return redirect("Payment_data")
