from django.urls import URLPattern, path
from . import views 

urlpatterns =[
    path('',views.home,name="homepage"),
    path('propertylist',views.propertylist,name="propertylist"),
    path('propertydetails',views.propertydetails,name="propertydetails"),
    path('tenantdetails',views.tenantdetails,name="tenantdetails")
]