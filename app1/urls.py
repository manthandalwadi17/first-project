from django.urls import path
from .views import *

urlpatterns = [
    path('',Company_Login,name='c_login'),
    path('Company_Regi',Company_Regi,name='c_regi'),
    path('CompForgetPass/',CompForgetPass,name='CompForgetPass'),
    path('OTP_checker',OTP_checker,name='OTP_checker'),
    path('Create_NewPass/',Create_NewPass,name='Create_NewPass'),
    path('DashBoard/',CompDashBoard,name='CompDashBoard'),
    path('Profile_Manage/',Profile_Manage,name='Profile_Manage'),
    path('AddCompCustom/',AddCompCustom,name='AddCompCustom'),
    path('ViewCustomers/',ViewCustomers,name='ViewCustomers'),
    path('DeleteCustomer/<int:id>',DeleteCustomer,name='DeleteCustomer'),
    path('ViewOrders/',ViewOrders,name='ViewOrders'),
    path('YEsOrder/<int:id>',YEsOrder,name='YEsOrder'),
    path('NoOrder/<int:id>',NoOrder,name='NoOrder'),
    path('ComLogout',ComLogout,name='ComLogout'),
    
    # ---------------- Product
    path('AddProduct/',AddProduct,name='AddProduct'),
    path('ViewProduct/',ViewProduct,name='ViewProduct'),
    path('DeleteProduct/<int:id>',DeleteProduct,name='DeleteProduct'),
    path('UpdateProduct/<int:id>',UpdateProduct,name='UpdateProduct'),
    
    # ---------------- customer --------------
    path('Customer_Login/',Customer_Login,name='Customer_Login'),
    path('Customer_dash/',Customer_dash,name='Customer_dash'),
    path('profile/',profile,name='profile'),
    path('Order_place/<int:id>',Order_place,name='Order_place'),
    path('All_Orders/',All_Orders,name='All_Orders'),
    path('Customer_logout/',Customer_logout,name='Customer_logout'),
]