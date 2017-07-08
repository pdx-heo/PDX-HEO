from django.contrib import admin
from .models import Organization
from .models import Shelter


admin.site.register(Organization)
admin.site.register(Shelter)
