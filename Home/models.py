from django.db import models
from django.contrib.auth.models import User
from landdeals.models import Properties
# Create your models here.

class Block_1(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(User,on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=255)
    Blockhash = models.CharField(max_length=255)
    
class Block_2(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(Block_1,on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=255)
    MedicineBlock = models.ForeignKey(Properties,on_delete=models.CASCADE)
    Blockhash = models.CharField(max_length=255)
    
class Block_3(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(Block_2,on_delete=models.CASCADE)
    MedicineBlock = models.ForeignKey(Properties,on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=255)
    Blockhash = models.CharField(max_length=255)
    
class Block_4(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(Block_3,on_delete=models.CASCADE)
    MedicineBlock = models.ForeignKey(Properties,on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=255)
    Blockhash = models.CharField(max_length=255)
