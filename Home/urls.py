from django.urls import path 
from .import views
urlpatterns = [
    path("",views.Index,name="Index"),
    path("LandLoardIndex",views.LandLoardIndex,name="LandLoardIndex"),
    path('SignIn',views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("UserTypeConfirmation",views.UserTypeConfirmation,name="UserTypeConfirmation"),
    path("LandLoadConfirm",views.LandLoadConfirm,name="LandLoadConfirm"),
    path("TenentConfirm",views.TenentConfirm,name="TenentConfirm"),
    path("SearchProperty",views.SearchProperty,name="SearchProperty")
]
