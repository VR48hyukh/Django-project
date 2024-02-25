from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from Service.Document.models import Sensor
from Service.api.serializers import SensorSerializerAPI


# Create your views here.
class SensorViewSet(APIView):
    def get(self, request):
        queryset=Sensor.objects.all()
        serializer_class=SensorSerializerAPI
        return Response({'posts': SensorSerializerAPI(queryset, many=True).data})

    def post(self, request):
        serializer=SensorSerializerAPI(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new=SensorSerializerAPI.create(
            name=request.data['name']
        )
        return Response({'posts': SensorSerializerAPI(post_new).data})


class ListSensor(APIView):
    queryset=Sensor.objects.all()
    serializer_class=ListSensorSerializer
