"""
MIT License
Copyright (c) 2017 Mackenzie Wangenstein, Chitradevi Maruthavanan, Andy Mayer


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from django.contrib import admin
from .models import Organization
from .models import ServiceType
from .models import Service
from .models import Testimony

# Register your models here.

class TestimonyAdmin(admin.ModelAdmin):
    fieldsets = [('Testimony Details', {'fields': ['title', 'story', 'author']})
    ]
    list_display = ('title', 'story', 'author')
    search_fields=('title', 'author')

class ServiceInline(admin.TabularInline):
  model = Service
  extra = 1


class OrganizationAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Contact Details', {'fields': ['phone', 'website', 'email']}),
  ]
  inlines = [ServiceInline]
  list_display = ('name', 'address', 'pub_date', 'updated_date')
  list_filter = ['pub_date', 'updated_date']
  search_fields = ['name']


class ServiceAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Organization', {'fields': ['organization']}),
    ('Service Type', {'fields': ['type']}),
    ('Service Details', {'fields': ['name', 'description', 'address', 'hours_open', 'hours_close']}),
    ('Contact Details', {'fields': ['phone', 'website', 'email']}),
  ]
  list_display = ('name', 'organization', 'type', 'address', 'pub_date', 'updated_date')
  list_filter = ['pub_date', 'updated_date', 'type']
  search_fields = ['name']


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ServiceType)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimony, TestimonyAdmin)
