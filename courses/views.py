from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from courses.forms import CourseForm
from courses.models import Course

@login_required
def course_inscription(request):
    if request.method == 'GET':
        form= CourseForm()
        context={
            'form': form,
        }
        return render(request, 'course/courses_inscription.html', context=context)
    elif request.method == 'POST':
        form= CourseForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                course=form.cleaned_data['course'],
                name= form.cleaned_data['name'],
                last_name= form.cleaned_data['last_name'],
                document = form.cleaned_data['document'],
                number_document=form.cleaned_data['number_document'],
                birth_date=form.cleaned_data['birth_date'],
                email=form.cleaned_data['email'],
            )
            context={
                'message':'La inscripcion se ha completado correctamente',
            }
            return render(request, 'course/courses_inscription.html', context=context)

        context={
            'errors':form.errors,
            'form':CourseForm(),
        }
        
        return render(request, 'course/courses_inscription.html', context=context)

def course(request):
    return render(request, 'course/course.html', context={})