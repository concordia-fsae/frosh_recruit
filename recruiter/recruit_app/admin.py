from django.contrib import admin
from .models import Form_Response, Team
from .helpers.sql_helpers import export_csv

# Register your models here.

@admin.register(Form_Response)
class FormResponseAdmin(admin.ModelAdmin):
    fieldsets= [
        ('Contact Information',         {'fields':['first_name', 'last_name', "email"]}),
        ('Interested In',               {'fields':['interests']}),
        ('Program Info',                {'fields':['program', 'year']}),
    ]
    
    ordering = ('first_name',)
    list_display = ('first_name', 'last_name', 'program', 'year')
    list_filter = ('program', 'year', 'interests')
    search_fields = ['first_name', 'last_name', 'email']
    filter_horizontal = ['interests']
    actions = [export_csv]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ordering = ('team_name',)
    list_display = ('team_name', 'value')
admin.site.site_header = "SAE Recruitment App Admin Page"
admin.site.site_title = "Admin Page"




