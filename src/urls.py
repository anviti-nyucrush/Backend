from django.contrib import admin
from django.urls import path
from login.views import (
    loginView, loginOptionsView, loginNumberView,
    loginOtpError, loginOtpVerify, loginLocation
)  
from profilesBasic.views import (
    profileBasic, profileAdvanced,
    managePhotos , selectSource, aboutYou
) 
from homescreen.views import(
    advanceFilter, Filter, suscribeElite, elite_register1,
    elite_register2, elite_register3, elite_register4,
    elite_register5,elite_payment, home
)

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #login endpoints
    path('login/', loginView),
    path('login/options', loginOptionsView),
    path('login/number', loginNumberView),
    path('login/number/otp', loginOtpVerify),
    path('login/number/otp/error', loginOtpError),   
    path('login/location', loginLocation),  

    #profile basic endpoints
    path('profile/basic', profileBasic),
    path('profile/advanced', profileAdvanced),
    path('profile/photos', managePhotos),
    path('profile/photos/source', selectSource),
    path('profile/about', aboutYou),

    #homescreen
    path('home/filter', Filter),
    path('home/filter/adv', advanceFilter),
    path('home/elite/subscribe', suscribeElite),
    path('home/elite/register1', elite_register1),
    path('home/elite/register2', elite_register2),
    path('home/elite/register3', elite_register3),
    path('home/elite/register4', elite_register4),
    path('home/elite/register5', elite_register5),
    path('home/elite/payment', elite_payment),
    path('home/', home),
    
    

    
]
