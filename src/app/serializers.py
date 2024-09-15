from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'slug', 'age', 'address', 'grade', 'major']
