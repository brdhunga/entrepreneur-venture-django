from django.contrib import admin
from venture.models import Venture, Profile




class VentureAdmin(admin.ModelAdmin):
    class Meta:
        model = Venture
admin.site.register(Venture, VentureAdmin)




class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile
admin.site.register(Profile, ProfileAdmin)
