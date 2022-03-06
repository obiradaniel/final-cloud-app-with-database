from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 10
    ordering = ('-question',)

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


# <HINT> Register Question and Choice models here
    
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('lesson', 'question', 'grade')
    list_filter = ['lesson']
    search_fields = ['lesson', 'question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'correct')
    list_filter = ['content']
    search_fields = ['content']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)