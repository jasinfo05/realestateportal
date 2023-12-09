from django.contrib import admin

from . models import Property
from . models import Unit
from . models import Tenant

admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)

