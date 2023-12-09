from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=100)
    features = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property_unit = models.ForeignKey('Property', related_name='units', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type} - {self.property_unit.name}"

class Tenant(models.Model):
    unit_tenant = models.ForeignKey('Unit', related_name='tenants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proofs = models.TextField()  
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()

    

    def __str__(self):
        return self.name

