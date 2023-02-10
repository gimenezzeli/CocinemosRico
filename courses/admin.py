from django.contrib import admin
from courses.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('course','name', 'last_name', 'document', 'number_document', 'birth_date', 'email')
    