from django.db import models

class Weight_enter(models.Model):
    user= models.CharField(max_length=20)
    weight= models.DecimalField(max_digits=5, decimal_places=1)
    date= models.DateTimeField(auto_now_add= True)