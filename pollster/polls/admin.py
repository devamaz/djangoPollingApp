from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.site_header ="Polling System Admin"
admin.site.site_title = "Polling System Admin Area"
admin.site.index_title = "Welcome to Admin Dashboard"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}), 
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines =[ChoiceInline]

admin.site.register(Question, QuestionAdmin)