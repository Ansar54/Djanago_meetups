from django.contrib import admin
from .models import Meetup,Participant

class CustomAdmin(admin.ModelAdmin):
    list_filter=('title','date')
    prepopulated_fields={'slug':('title','location'),}
admin.site.register(Meetup,CustomAdmin)

