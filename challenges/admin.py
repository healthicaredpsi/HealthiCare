from django.contrib import admin
from.models import Challenge,Winner,Reward
# Register your models here.
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name','description','start_time','end_time']
    list_display_links = ['name','description']
    list_per_page = 5

#@admin.site.register(models.Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['description','credit_no']
    list_display_links = ['description','credit_no']
    #list_editable = ['credit_no']
    list_per_page = 5

class WinnerAdmin(admin.ModelAdmin):
    list_display=['challenge']
    list_display_links = [ 'challenge']

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Winner,WinnerAdmin)
