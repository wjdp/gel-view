from django.contrib import admin
from gel_view.models import *

class GelRefAdmin(admin.ModelAdmin):
	pass

class GelAdmin(admin.ModelAdmin):
	pass

admin.site.register(GelRef, GelRefAdmin)
admin.site.register(Gel, GelAdmin)