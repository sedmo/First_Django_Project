from django.contrib import admin

# Register your models here.
from .models import Choice, Question


# This tells Django: “Choice objects are 
# edited on the Question admin page. 
# By default, provide enough fields for 3 choices.”

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

# btw, create a model admin class any time
# you need to change the admin options for a model.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
