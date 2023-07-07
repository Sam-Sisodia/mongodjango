from rest_framework import serializers

from .models import  *

class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields= "__all__"



class SchoolSerilizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields= ["id","name","school_address","school_contact"]
