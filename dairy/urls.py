from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
        path('contact/', views.ContactUs, name='home'),
        path('signup/', views.signup, name='signup'),
        path('addcustomer/',views.addcustomer,name='addcustomer'),
        path('allcustomer/',views.allcustomer,name='allcustomer'),
        path('Customer_page/',views.Customer_page,name='Customer_page'),
        path('customer_ledger_save/', views.customer_ledger_save, name='customer_ledger_save'),
        path('customer_ledger_delete/',views.customer_ledger_delete,name='customer_ledger_delete'),
        path('customer_milk_category/',views.customer_milk_category,name='customer_milk_category'),
        path('customer_ledger/<int:pk>/', views.customer_ledger, name='customer_ledger'),
        path('allvendor/', views.allvendor, name='allvendor'),
        path('addvendor/', views.addvendor, name='addvendor'),
        path('add_milk_category/',views.add_milk_category, name='add_milk_category'),
        path('ledger_save/',views.ledger_save,name='ledger_save'),
        path('ledger_delete/',views.ledger_delete,name='ledger_delete'),
        path('ledger/<int:pk>/', views.ledger, name='ledger'),
        path('home/', views.home, name='home'),
        path('', LoginView.as_view(), name='login'),
]
