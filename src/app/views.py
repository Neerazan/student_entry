from django.shortcuts import get_object_or_404, redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'major']
    search_fields = ['name', 'major']
    ordering_fields = ['name', 'age', 'major']

    def get_queryset(self):
        return Student.objects.all()

    lookup_field = 'slug'


# Template Views
def student_list_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students, 'form': form})


def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_detail.html', {'student': student, 'form': form})


def student_delete(request, slug):
    student = get_object_or_404(Student, slug=slug)
    student.delete()
    return redirect('student-list')
