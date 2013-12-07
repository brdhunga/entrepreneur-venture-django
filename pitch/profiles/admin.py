from django.contrib import admin
from profiles.models import ProfileDetail

class ProfileDetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProfileDetail, ProfileDetailAdmin)