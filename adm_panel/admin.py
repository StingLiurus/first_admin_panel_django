from django.contrib import admin 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

class SearchIssue(admin.ModelAdmin):
    search_fields = ["title"]

class SearchNewsEvents(admin.ModelAdmin):
    search_fields = ["title"]

class SearchPeople(admin.ModelAdmin):
    search_fields = ["name"]

admin.site.register(Issue,SearchIssue)
admin.site.register(NewsEvents,SearchNewsEvents)
admin.site.register(People,SearchPeople)
admin.site.register(Requests)
admin.site.register(SiteFace)
admin.site.register(SiteFaceEn)
admin.site.register(Structure)
admin.site.register(Vacanc)

