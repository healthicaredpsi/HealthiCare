from django.contrib import admin
from .models import Meditation,Breath

# Register your models here.

class MeditationAdmin(admin.ModelAdmin):
    list_display = ['duration','time']
    list_display_links = ['duration', 'time']

#@admin.site.register(models.Breath)
class BreathAdmin(admin.ModelAdmin):
    list_display = ['time','duration']
    list_display_links = ['time','duration']
    #list_editable = ['time','duration']
    list_per_page = 10

admin.site.register(Breath,BreathAdmin)
admin.site.register(Meditation,MeditationAdmin)