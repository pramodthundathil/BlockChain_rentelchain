from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import PropertyAddForm
from .models import Properties,PersonalDetailsLeaser,PersonalDetailsLandloard,RentelApprovel,Contarct,Contract_Block1,Contract_block2
from Home.models import Block_1, Block_2, Block_3, Block_4
from Home.blockgenerator import Block
from datetime import datetime
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest


razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# Create your views here.
@login_required(login_url='SignIn')
def MyProperties(request):
    proper = Properties.objects.filter(user  = request.user)
    context = {
        "proper":proper
    }
    return render(request,"myproperties.html",context)

@login_required(login_url='SignIn')
def Propertyadd(request):
    form = PropertyAddForm()
    if request.method == "POST":
        form = PropertyAddForm(request.POST,request.FILES)
        if form.is_valid:
            formdata = form.save()
            formdata.user = request.user 
            formdata.status = "listed"
            formdata.save() 
            
            item = Properties.objects.get(id = formdata.id)
            
            # block 2 Creation for login data
            
            user = request.user 
            logdata = {"name":user.first_name,"username":user.username,"password":user.password,"medicine":item}
            regblock = Block_1.objects.get(BlockLink = request.user)
            
            BlockChain = Block(2, datetime.now(), logdata,regblock.Blockhash)
            
            block2 = Block_2.objects.create(BlockIndex = 2,BlockTimeStrap = datetime.now(),BlockData=logdata,BlockLink = regblock,previous_hash = regblock.Blockhash,Blockhash = BlockChain.hash,MedicineBlock = item)
            block2.save()
            
            # Block 3 creation property data.....
            
            meddata = {"name":item.name,"price":item.rentpermomth,"place":item.place,"addeddate":item.date,"state":item.state}
            
            BlockChanin2 = Block(3,item.date,meddata,block2.Blockhash)
            
            block3 = Block_3.objects.create(BlockIndex = 3, BlockTimeStrap = datetime.now(),BlockData = meddata,BlockLink = block2,MedicineBlock = item,previous_hash = block2.Blockhash,Blockhash = BlockChanin2.hash )
            block3.save()
            
            # Block $ Creation Consolidated data
            
            blockdata = [regblock,block2,block3]
            
            BlockChanin3 = Block(4,"time",blockdata,block3.Blockhash)
            block4 = Block_4.objects.create(BlockIndex = 4,BlockTimeStrap = datetime.now(),BlockData = blockdata,BlockLink = block3,MedicineBlock = item,previous_hash = block3.Blockhash,Blockhash = BlockChanin3.hash)
            block4.save()
            messages.success(request,"New Property Added To secured List")
            return redirect("MyProperties")
            

    return render(request,"propertyadd.html",{"form":form})

@login_required(login_url='SignIn')
def DeleteProperty(request,pk):
    Properties.objects.get(id = pk).delete()
    messages.success(request,"Property Deleted SuccessFully")
    return redirect("MyProperties")

@login_required(login_url='SignIn')
def PropertyValidation(request,pk):
    item = Properties.objects.get(id = pk)
    block4 = Block_4.objects.get(MedicineBlock = item)
    block3 = Block_3.objects.get(MedicineBlock = item)
    block2 = Block_2.objects.get(MedicineBlock = item)
    block1 = block2.BlockLink
    
    propdata = {"name":item.name,"price":item.rentpermomth,"place":item.place,"addeddate":item.date,"state":item.state}
    BlockChanin2 = Block(3,item.date,propdata,block2.Blockhash)
    
    blockdata = [block1,block2,block3]
    blockhashvalue = Block(4,"time",blockdata,block3.Blockhash)
    print(blockhashvalue)
    if BlockChanin2.hash == block3.Blockhash:
        if blockhashvalue.hash == block4.Blockhash:
            messages.success(request,"The Property {} is valid".format(item.name))
            return redirect("MyProperties")
        else:
            messages.info(request,"The Property {} is not valid".format(item.name))
            return redirect("MyProperties")
    else:
        messages.info(request,"The Property {} is not valid".format(item.name))
        return redirect("MyProperties")
    
@login_required(login_url='SignIn')
def MyRentels(request):
    user = request.user
    
    requests = RentelApprovel.objects.filter(landloard = user.id)
    
    context = {
        "requests":requests,
    }
    try:
        contract = Contarct.objects.filter(landloard = request.user)
        context["contract"] = contract
    except:
        pass
    return render(request,"myrentels.html",context)


def ViewProperty(request,pk):
    proper = Properties.objects.get(id =pk)
    context = {
        "proper":proper
    }
    return render(request,"propertysingleview.html",context)

def CustomerValidation(request,pk):
    item = Properties.objects.get(id =pk)
    item = Properties.objects.get(id = pk)
    block4 = Block_4.objects.get(MedicineBlock = item)
    block3 = Block_3.objects.get(MedicineBlock = item)
    block2 = Block_2.objects.get(MedicineBlock = item)
    block1 = block2.BlockLink
    
    propdata = {"name":item.name,"price":item.rentpermomth,"place":item.place,"addeddate":item.date,"state":item.state}
    BlockChanin2 = Block(3,item.date,propdata,block2.Blockhash)
    
    blockdata = [block1,block2,block3]
    blockhashvalue = Block(4,"time",blockdata,block3.Blockhash)
    print(blockhashvalue)
    if BlockChanin2.hash == block3.Blockhash:
        if blockhashvalue.hash == block4.Blockhash:
            messages.success(request,"The Property {} is valid".format(item.name))
            return redirect("ViewProperty",pk= pk)
        else:
            messages.error(request,"The Property {} is not valid".format(item.name))
            return redirect("ViewProperty",pk= pk)
    else:
        messages.error(request,"The Property {} is not valid".format(item.name))
        return redirect("ViewProperty",pk= pk)
    
@login_required(login_url='SignIn')
def RequestforRentel(request,pk):
    item = Properties.objects.get(id =pk)
    item = Properties.objects.get(id = pk)
    block4 = Block_4.objects.get(MedicineBlock = item)
    block3 = Block_3.objects.get(MedicineBlock = item)
    block2 = Block_2.objects.get(MedicineBlock = item)
    block1 = block2.BlockLink
    
    propdata = {"name":item.name,"price":item.rentpermomth,"place":item.place,"addeddate":item.date,"state":item.state}
    BlockChanin2 = Block(3,item.date,propdata,block2.Blockhash)
    
    blockdata = [block1,block2,block3]
    blockhashvalue = Block(4,"time",blockdata,block3.Blockhash)
    print(blockhashvalue)
    context = {
        "proper":item
    }
    if BlockChanin2.hash == block3.Blockhash:
        if blockhashvalue.hash == block4.Blockhash:
            # messages.success(request,"The Property {} is valid".format(item.name))
            if RentelApprovel.objects.filter(properties = item, user = request.user).exists():
                messages.success(request,"Rentel Request is Already Submited for approval")
                return redirect("ViewProperty", pk = pk)
            else:
                return redirect('RentelForm',pk=pk)
        else:
            messages.error(request,"The Property {} is not valid You Cannot rent this property".format(item.name))
            return redirect("ViewProperty",pk= pk)
    else:
        messages.error(request,"The Property {} is not valid You Cannot rent this property".format(item.name))
        return redirect("ViewProperty",pk= pk)
    
@login_required(login_url='SignIn')
def RentelForm(request,pk):
    item = Properties.objects.get(id =pk)
    if request.method == "POST":
        name = request.POST["name"]
        place = request.POST["place"]
        district = request.POST["district"]
        state = request.POST["state"]
        country = request.POST["contry"]
        phone = request.POST["phone"]
        pro_pic = request.FILES["photo"]
        idproof = request.FILES["idproof"]
        if RentelApprovel.objects.filter(properties = item, user = request.user).exists():
            messages.success(request,"Rentel Request is Already Submited for approval")
            return redirect("ViewProperty", pk = pk)
        else:
            leaser = PersonalDetailsLeaser.objects.create(name = name,place=place,district = district,state = state,country = country,phone = phone, pro_pic = pro_pic, idproof = idproof,user = request.user )
            leaser.save()
            
            approval = RentelApprovel.objects.create(properties = item,leaser = leaser,landloard = item.user.id,user = request.user )
            approval.save()
            messages.success(request,"Rentel Request was Created")
            return redirect("ViewProperty", pk = pk)
            
    context = {
        "proper":item
    }
    return render(request,'requestforrent.html',context)

@login_required(login_url='SignIn')
def ApproveRentrequest(request,pk):
    if PersonalDetailsLandloard.objects.filter(user = request.user).exists():
        landlaordprofile = PersonalDetailsLandloard.objects.get(user = request.user)
        rentrequest = RentelApprovel.objects.get(id = pk)
        leaser_regblock = Block_1.objects.get(BlockLink = rentrequest.user )
        
        
        contract = Contarct.objects.create(leaser_name = rentrequest.leaser.name,landloard_name = landlaordprofile.name,date = datetime.now(),properties = rentrequest.properties, rent = rentrequest.properties.rentpermomth,leaser = rentrequest.user.id,landloard = request.user)
        contract.save()
        propertitem = rentrequest.properties
        propertitem.status = "On Rentel"
        propertitem.save()
        
        rentrequest.delete()
        
        # Block one already have the registration block it will validate at the time of contract validation
        # Contract Block 2 Creation
        
        landload_regblock = Block_1.objects.get(BlockLink = request.user)
        
        blockdata = {"leaser" :contract.leaser_name,"landloard" : contract.landloard_name,"rent":contract.rent}
        BlockChain1 = Block(2, "time", blockdata,landload_regblock.Blockhash)
        
        block1_contract = Contract_Block1.objects.create(BlockIndex = "2",BlockData = blockdata, BlockLink = contract,previous_hash_leaser = leaser_regblock.Blockhash,previous_hash_landlaord = landload_regblock.Blockhash, Blockhash = BlockChain1.hash)
        block1_contract.save()
        
        # Block 2 Contract creation
        
        blockdata2 = [leaser_regblock,block1_contract]
        blockchain2 = Block(3,"time",blockdata2,block1_contract.Blockhash)
        block2_contract = Contract_block2.objects.create(BlockIndex = "2",BlockData = blockdata2,BlockLink = contract,previous_hash = block1_contract.Blockhash,Blockhash = blockchain2.hash )
        block2_contract.save()
        
        
        messages.info(request,"Rentel Contract Created")
        return redirect('MyRentels')
    else:
        messages.info(request,"You Dont have profile data please fill it and try agin")
        return redirect('MyRentels')
    
def Landloardprofile(request):
    try:
        profile = PersonalDetailsLandloard.objects.get(user = request.user)
        context = {
        "profile":profile
        }
        return render(request,"landloardprofile.html",context)
    except:
        return redirect("PersonaldetailsLandloard")
    
@login_required(login_url='SignIn')
def PersonaldetailsLandloard(request):
    if request.method == "POST":
        name = request.POST["name"]
        place = request.POST["place"]
        district = request.POST["district"]
        state = request.POST["state"]
        country = request.POST["contry"]
        phone = request.POST["phone"]
        pro_pic = request.FILES["photo"]
        idproof = request.FILES["idproof"]
        if PersonalDetailsLandloard.objects.filter(user = request.user).exists():
            pdata = PersonalDetailsLandloard.objects.get(user = request.user)
            pdata.name = name 
            pdata.place = place
            pdata.district = district
            pdata.state = state
            pdata.country = country
            pdata.phone = phone 
            pdata.pro_pic.delete()
            pdata.pro_pic = pro_pic
            pdata.idproof.delete()
            pdata.idproof = idproof
            pdata.save()
            messages.info(request,"Profile Updated")
            return redirect("Landloardprofile")
        else:
            landloard = PersonalDetailsLandloard.objects.create(name = name,place=place,district = district,state = state,country = country,phone = phone, pro_pic = pro_pic, idproof = idproof,user = request.user )
            landloard.save()
            messages.info(request,"Profile Updated")
            return redirect("Landloardprofile")
            
    return render(request,"profiledataforlandloard.html")


def ContractvalidationCheck(request,pk):
    contract = Contarct.objects.get(id = pk)
    landload_regblock = Block_1.objects.get(BlockLink = request.user)
    b2 = Contract_block2.objects.get(BlockLink = contract)
    b3 = Contract_block2.objects.get(BlockLink = contract)
    blockdata = {"leaser" :contract.leaser_name,"landloard" : contract.landloard_name,"rent":contract.rent}
    
    BlockChain1 = Block(2, "time", blockdata,landload_regblock.Blockhash)
    if b3.previous_hash == BlockChain1.hash:
        contract.contract_status = True
        contract.save()
        return redirect('MyRentels')
    else:
        print("my--------")
        contract.contract_status = False
        contract.save()
        return redirect('MyRentels')
    
def Myrentelslease(request):
    context = {}
    
    try:
        contract = Contarct.objects.filter(leaser = int(request.user.id))
        context["contract"] = contract
    except:
        pass
    return render(request,"myrentelsleaser.html",context)

def ContractvalidationCheckLeaser(request,pk):
    contract = Contarct.objects.get(id = pk)
    landload_regblock = Block_1.objects.get(BlockLink = contract.landloard)
    b2 = Contract_block2.objects.get(BlockLink = contract)
    b3 = Contract_block2.objects.get(BlockLink = contract)
    blockdata = {"leaser" :contract.leaser_name,"landloard" : contract.landloard_name,"rent":contract.rent}
    
    BlockChain1 = Block(2, "time", blockdata,landload_regblock.Blockhash)
    if b3.previous_hash == BlockChain1.hash:
        contract.contract_status = True
        contract.save()
        return redirect('Myrentelslease')
    else:
        print("my--------")
        contract.contract_status = False
        contract.save()
        return redirect('Myrentelslease')
    
def Payrent(request,pk):
    contract = Contarct.objects.get(id = pk)
    currency = 'INR'
    amount = contract.rent * 100 # Rs. 200
    context = {}

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = "http://127.0.0.1:8000/landdeals/paymenthandler/"

  # we need to pass these details to frontend.
    
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = "1",
    # context['numitems'] = len(checkitems)
    # context['total'] = total
    context["contract"] = contract
    
    return render(request,"payrent.html",context)


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

      # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 20000 * 100 # Rs. 200
                try:
                    print("working 1")
                    razorpay_client.payment.capture(payment_id, amount)
                    return redirect('Myrentelslease')
          # render success page on successful caputre of payment
                except:
                    print("working 2")
                    return redirect('Myrentelslease')
                    
                    
          # if there is an error while capturing payment.
            else:
                return render(request, 'paymentfail.html')
        # if signature verification fails.    
        except:
            return HttpResponseBadRequest()
        
      # if we don't find the required parameters in POST data
    else:
  # if other than POST request is made.
        return HttpResponseBadRequest()
        
        
    
    
    
    
    
    
    
    