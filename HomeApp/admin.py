from django.contrib import admin
from HomeApp.models import Participant

# Register your models here.


class AdminParticipant(admin.ModelAdmin):
    list_display = ['nickname', 'poty', 'moty']  # COL DATA
    search_fields = ['nickname']  # SEARCH DATA
    list_filter = ['poty', 'moty']  # FILTER


admin.site.register(Participant, AdminParticipant)
