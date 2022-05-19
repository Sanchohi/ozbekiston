from django.contrib import admin
from .models import *
# Register your models here.
class ViloyatAdmin(admin.ModelAdmin):
	list_display = ('id','name',)
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Viloyat,ViloyatAdmin)

class RayonAdmin(admin.ModelAdmin):
	list_display = ('id','name','cat')

	prepopulated_fields = {'slug':('name',)}

admin.site.register(Rayon,RayonAdmin)

class UmumiyAdmin(admin.ModelAdmin):
	list_display = ('id','name','cat')

	prepopulated_fields = {'slug':('name',)}

admin.site.register(Umumiy,UmumiyAdmin)