from rest_framework.views import APIView
from .models import Payment_details
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
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
    data = serialize.data    
    url = "https://www.onlinesbi.com/sbicollect/icollecthome.htm?corpID=3802557"
    web = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver') # system path of chromedriver
    web.get(url) 
    check_box = web.find_element_by_xpath('//*[@id="proceedcheck_english"]')
    check_box.click()
    time.sleep(0.80)
    proceed_btn = web.find_element_by_xpath('//*[@id="welcomecollect_english"]/div[2]/button')
    proceed_btn.click()
    time.sleep(0.80)
    dropclick = web.find_element_by_xpath('//*[@id="frmFeeParams"]/div/div/div[2]/div/div[2]/div/button/span[1]')
    dropclick.click()
    dropdown = web.find_element_by_xpath('//*[@id="frmFeeParams"]/div/div/div[2]/div/div[2]/div/div/ul/li[2]/a')
    dropdown.click()
    name = data['name']
    name_input = web.find_element_by_xpath('//*[@id="outref11"]')
    name_input.send_keys(name)
    mobile_number = data['mobile']
    mobile_input = web.find_element_by_xpath('//*[@id="outref12"]')
    mobile_input.send_keys(mobile_number)
    email = data['email']
    email_input = web.find_element_by_xpath('//*[@id="outref13"]')
    email_input.send_keys(email)
    amount = data['amount']
    amount_input = web.find_element_by_xpath('//*[@id="outref14"]')
    amount_input.send_keys(amount)
    remarks = data['remarks']
    remarks_input = web.find_element_by_xpath('//*[@id="transactionRemarks"]')
    remarks_input.send_keys(remarks)
    Cust_name = data['name']
    name_input = web.find_element_by_xpath('//*[@id="cusName"]')
    name_input.send_keys(Cust_name)
    dob = web.find_element_by_xpath('//*[@id="frmFeeParams"]/div[2]/div/div[3]/div[2]/div/div[2]/img')    
    dob.click()
    select_year = Select(web.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]'))
    select_year.select_by_value('2000')
    select_month = Select(web.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]'))
    select_month.select_by_value('9')
    lst = [['01','02', '03', '04', '05' ,'06' ,'07'],
    ['08','09' ,'10' ,'11' ,'12' ,'13' ,'14'],
    ['15' ,'16' ,'17' ,'18' ,'19' ,'20' ,'21'], 
    ['22' ,'23' ,'24' ,'25' ,'26' ,'27' ,'28'],
    ['29' ,'30' ,'31']]
    value = '13'
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                print(i+1,j+1)
                select_day = web.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[{j}]/td[{i}]/a'.format(j=i+1,i=j+1))
                select_day.click()

    mobile_number = data['mobile']
    Cust_mobile_input = web.find_element_by_xpath('//*[@id="mobileNo"]')
    Cust_mobile_input.send_keys(mobile_number)

    email = data['email']
    Cust_email_input = web.find_element_by_xpath('//*[@id="emailId"]')
    Cust_email_input.send_keys(email)


    time.sleep(5)
    return Response(data = data,status = status.HTTP_200_OK)




    
    
    
    
