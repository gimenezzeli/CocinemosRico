from django import forms
from courses.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields=['course','name','last_name','document','number_document', 'birth_date', 'email']