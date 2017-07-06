from django.contrib import admin
from .models import ServiceType
from .models import Organization
from .models import Service


admin.site.register(ServiceType)
admin.site.register(Organization)
admin.site.register(Service)
