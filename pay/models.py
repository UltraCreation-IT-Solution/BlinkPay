from django.db import models
from django.db.models.signals import pre_save
from .utils import *
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Payment_details(models.Model):
    card_id         = models.CharField(max_length=20,verbose_name="Card ID",unique=True,blank=True)
    name            = models.CharField(max_length=50 , verbose_name="Name")
    txt_id          = models.CharField(max_length=50, verbose_name="Text ID")
    txt_count       = models.IntegerField(verbose_name="Text Count")
    mobile          = PhoneNumberField(verbose_name="Phone NO")
    email           = models.EmailField(verbose_name="Email")
    amount          = models.PositiveIntegerField(verbose_name="Amount")
    dob             = models.CharField(max_length=20,verbose_name="Date of Birth" )
    remarks         = models.CharField(max_length=80,verbose_name = 'Remarks',blank=True) 
    card_no         = models.PositiveIntegerField(verbose_name="Card No")
    month           = models.PositiveIntegerField(verbose_name="Month")
    year            = models.PositiveIntegerField(verbose_name="Year")
    cvv             = models.PositiveIntegerField(verbose_name="CVV")
    ipin            = models.PositiveIntegerField(verbose_name="IPIN")
    transaction_id  = models.CharField(max_length=30,verbose_name="Transaction ID")
    status          = models.BooleanField(verbose_name="Status",default=False)
    
    def __str__(self):
        return self.name

def pre_save_create_card_id(sender, instance, *args, **kwargs):
    if not instance.card_id:
        instance.card_id= unique_card_id_generator(instance)


pre_save.connect(pre_save_create_card_id, sender=Payment_details)