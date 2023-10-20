from rest_framework.response import Response
from .serializers import LocationSerializer
from .models import Location
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def LocationList(request):
    if request.method=='GET':
        location=Location.objects.all()
        serializer=LocationSerializer(location, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        serializer=LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def locationDetails(request,pk):
    try:
        location=Location.objects.get(id=pk)
    except location.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=LocationSerializer(location)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)