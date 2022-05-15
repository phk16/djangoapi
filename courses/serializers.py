
from rest_framework import serializers
from .models import Course

class CourseSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields=('id', 'url', 'name', 'language', 'price')


