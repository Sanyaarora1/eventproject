from django.urls import path
from . import views

urlpatterns = [
    path('api/enquiry/', views.create_enquiry, name='create_enquiry'),
    path('', views.home, name='home'),
    path('enquiry/', views.enquiry_page, name='enquiry_page'),
    path('contact/', views.contact_page, name='contact_page'),
]
