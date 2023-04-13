from django.urls import path 
from .import views 
urlpatterns = [
    path("MyProperties",views.MyProperties,name="MyProperties"),
    path("Propertyadd",views.Propertyadd,name="Propertyadd"),
    path("DeleteProperty/<int:pk>",views.DeleteProperty,name="DeleteProperty"),
    path("PropertyValidation/<int:pk>",views.PropertyValidation,name="PropertyValidation"),
    path("MyRentels",views.MyRentels,name="MyRentels"),
    path("ViewProperty/<int:pk>",views.ViewProperty,name="ViewProperty"),
    path("CustomerValidation/<int:pk>",views.CustomerValidation,name="CustomerValidation"),
    path("RequestforRentel/<int:pk>",views.RequestforRentel,name="RequestforRentel"),
    path("RentelForm/<int:pk>",views.RentelForm,name="RentelForm"),
    path("ApproveRentrequest/<int:pk>",views.ApproveRentrequest,name="ApproveRentrequest"),
    path("PersonaldetailsLandloard",views.PersonaldetailsLandloard,name="PersonaldetailsLandloard"),
    path("Landloardprofile",views.Landloardprofile,name="Landloardprofile"),
    path("ContractvalidationCheck/<int:pk>",views.ContractvalidationCheck,name="ContractvalidationCheck"),
    path("Myrentelslease",views.Myrentelslease,name="Myrentelslease"),
    path("ContractvalidationCheckLeaser/<int:pk>",views.ContractvalidationCheckLeaser,name="ContractvalidationCheckLeaser"),
    path("Payrent/<int:pk>",views.Payrent,name="Payrent"),
    path("paymenthandler/",views.paymenthandler,name="paymenthandler")
    
    
]
