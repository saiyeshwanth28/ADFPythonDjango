from django.db import models

class requestForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DOb = models.CharField(max_length=15,default=None)
    gender = models.CharField(max_length=10,default=None)
    Nationality = models.CharField(max_length=30,default=None)
    State = models.CharField(max_length=30,default=None)
    Current_city = models.CharField(max_length=40,default=None)
    pin_code = models.IntegerField(default=None)
    Qualification = models.CharField(max_length=20,default=None)
    salary = models.IntegerField(default=None)
    pan_number = models.CharField(max_length=10,default=None)
    received_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'request_form'

class responseForm(models.Model):
    request_id = models.IntegerField(default=None)
    response = models.CharField(max_length=200)
    reason =models.CharField(max_length=300,default=None)

    class Meta:
        db_table = 'response_form'

