
from django.urls import path

from myApp.views import *

urlpatterns = [
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path("editProfile/", editProfile, name="editProfile"),

    
    
]