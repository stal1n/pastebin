from django.contrib import admin
from pastebin.apps.models import Paste

class PasteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paste, PasteAdmin)