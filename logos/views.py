from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LogoSerializer

from .models import Logo
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/logo-list/',
		'Detail View':'/logo-detail/<str:pk>/',
		'Create':'/logo-create/',
		'Update':'/logo-update/<str:pk>/',
		'Delete':'/logo-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def logoList(request):
	logos = Logo.objects.all().order_by('-id')
	serializer = LogoSerializer(logos, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def logoDetail(request, pk):
	logos = Logo.objects.get(id=pk)
	serializer = LogoSerializer(logos, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def logoCreate(request):
	serializer = LogoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def logoUpdate(request, pk):
	logo = Logo.objects.get(id=pk)
	serializer = LogoSerializer(instance=logo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def logoDelete(request, pk):
	logo = Logo.objects.get(id=pk)
	logo.delete()

	return Response('Item succsesfully delete!')