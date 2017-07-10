from django.contrib import admin
from .models import Organization
from .models import Shelter


class ShelterInline(admin.TabularInline):
  model = Shelter
  extra = 1


class OrganizationAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Publish', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ShelterInline]
  list_display = ('name', 'address', 'pub_date')
  list_filter = ['pub_date']
  search_fields = ['name']


class ShelterAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization', {'fields': ['organization']}),
    ('Shelter Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Shelter, ShelterAdmin)
