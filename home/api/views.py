from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import StudentSerializers
from ..models import StudentDetail

@api_view(['GET','POST'])
def StudInfo(request):
    if request.method == 'GET':
        data = StudentDetail.objects.all()
        serial = StudentSerializers(data,many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = StudentSerializers(data=request.data)
        if serial.is_valid():
            name = serial.data['name']
            regno = serial.data['regno']
            dept = serial.data['dept']
            gender = serial.data['gender']
            age = serial.data['age']
            data = StudentDetail.objects.create(
                name = name,
                regno = regno,
                dept = dept,
                gender = gender,
                age = age,
            )
            data.save()
            return Response("Successfully Added Student")
        else:
            return Response(serial.errors)
            

