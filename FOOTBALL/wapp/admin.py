from django.contrib import admin
from .models import Club,Match,Player,MatchEvent,PlayerProfile
# from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
admin.site.register(Club)
# admin.site.register(Player)
admin.site.register(Match)
admin.site.register(MatchEvent)
admin.site.register(PlayerProfile)


class PlayerProfileInline(admin.StackedInline):
    model = PlayerProfile
    # extra = 1
    
class PlayerModelAdmin(admin.ModelAdmin):
    inlines = [PlayerProfileInline]
    
    list_display = ['name', 'age', 'club']
    search_fields = ['name', 'club__name']
    list_filter = ['club']
    
admin.site.register(Player, PlayerModelAdmin)