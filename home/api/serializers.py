from django.db import models
from django.db.models import fields
from ..models import StudentDetail
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ['id','name','regno','dept','gender','age']
