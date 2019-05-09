from django.contrib import admin
from .models import Events

# Register your models here.
class AllEvents(admin.ModelAdmin):
    fields = ('event_title', 'event_location', 'event_date','event_description')
    save_as = True

admin.site.register(Events,AllEvents)
