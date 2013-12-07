from django.contrib import admin
from venture.models import Venture

class VentureAdmin(admin.ModelAdmin):
    pass
admin.site.register(Venture, VentureAdmin)