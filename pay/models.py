from django.db import models

# Create your models here.
class Payment_details(models.Model):
    name = models.CharField(max_length=50)
    txt_id = models.CharField(max_length=50)
    txt_count = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    amount =models.IntegerField()
    card_no = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    status = models.BooleanField()
    def __str__(self):
        return self.name