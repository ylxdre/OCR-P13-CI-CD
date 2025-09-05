from django.contrib import admin
from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile


class LettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'street', 'city', 'country_iso_code')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'favorite_city')

admin.site.register(Letting, LettingAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Profile, ProfileAdmin)
