from django.shortcuts import render, get_object_or_404
from .models import Property, Unit, Tenant

def home(request):
    return render(request, 'home.html')

def propertylist(request):
    Properties= Property.objects.all()
    return render(request, 'propertylist.html', {'properties':Properties})

def propertydetails(request):
    ID=request.GET['id']
    property_instance = get_object_or_404(Property, id=ID)
    property_units = Unit.objects.filter(property_unit=property_instance)
    return render(request, 'propertydetails.html', {'property_units': property_units})

def tenantdetails(request):
    ID=request.GET['id']
    unit_instance = get_object_or_404(Unit, id=ID)
    tenant_details = Tenant.objects.filter(unit_tenant=unit_instance)
    return render(request, 'tenantinfo.html', {'tenant_details': tenant_details})
