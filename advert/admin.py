from django.contrib import admin
from .models import Category, Location, Advantages, Surroundings, Advert, Banner

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Advantages)
admin.site.register(Surroundings)
# admin.site.register(Advert)
admin.site.register(Banner)

@admin.register((Advert))
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id','category','location','street','premium']
    list_editable = ['premium']
