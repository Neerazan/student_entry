from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    StudentViewSet,
    student_list_create,
    student_detail,
    student_delete,
)

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')


template_urlpatterns = [
    path('students-template/', student_list_create, name='student-list'),
    path('students-template/<slug:slug>/', student_detail, name='student-detail'),
    path('students-template/<slug:slug>/delete/', student_delete, name='student-delete'),
]

urlpatterns = [
    path('', include(router.urls)),
] + template_urlpatterns
