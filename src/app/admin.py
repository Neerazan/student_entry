from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'age', 'address', 'grade', 'major')
    search_fields = ('name', 'major')
    list_filter = ('major', 'grade')
    ordering = ('name',)

    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        return super().get_readonly_fields(request, obj) + ('slug',)
