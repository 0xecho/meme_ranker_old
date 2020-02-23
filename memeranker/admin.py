from django.contrib import admin
from .models import Meme
# Register your models here.

class MemeAdmin(admin.ModelAdmin):
	list_display=('uploader','likes')
	ordering = ('-likes',)
admin.site.register(Meme,MemeAdmin)
# admin.site.register()