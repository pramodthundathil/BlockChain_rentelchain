from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from Home.models import Block_1

class Properties(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    rentpermomth = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to="Property_image")
    status = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     
class PersonalDetailsLeaser(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.IntegerField()
    pro_pic = models.FileField(upload_to="leaser_pro_pic")
    idproof = models.FileField(upload_to="lease_id_proof")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class PersonalDetailsLandloard(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.IntegerField()
    pro_pic = models.FileField(upload_to="landloard_pro_pic")
    idproof = models.FileField(upload_to="landloard_id_proof")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class RentelApprovel(models.Model):
    date = models.DateField(auto_now_add=True)
    properties = models.ForeignKey(Properties,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    leaser = models.ForeignKey(PersonalDetailsLeaser,on_delete=models.CASCADE)
    landloard = models.IntegerField()
    
    
class Contarct(models.Model):
    leaser_name = models.CharField(max_length=255)
    landloard_name = models.CharField(max_length=255)
    properties = models.ForeignKey(Properties,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    rent = models.FloatField()
    leaser  = models.IntegerField()
    landloard = models.ForeignKey(User,on_delete=models.CASCADE)  
    contract_status = models.BooleanField(default=True)
    rent_status = models.BooleanField(default=True)
    
class Contract_Block1(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(Contarct,on_delete=models.CASCADE)
    previous_hash_leaser = models.CharField(max_length=255)
    previous_hash_landlaord = models.CharField(max_length=255)
    Blockhash = models.CharField(max_length=255)
    
class Contract_block2(models.Model):
    BlockIndex = models.CharField(max_length=20)
    BlockTimeStrap = models.DateTimeField(auto_now_add=True)
    BlockData = models.CharField(max_length=255)
    BlockLink = models.ForeignKey(Contarct,on_delete=models.CASCADE)
    previous_hash = models.CharField(max_length=255)
    Blockhash = models.CharField(max_length=255)
    
    
    
     
    
    
    
    
