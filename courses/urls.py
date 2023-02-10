from django.urls import path
from courses.views import course_inscription, course

urlpatterns = [
    path('our-course/', course),
    path('inscription-course/', course_inscription),
]