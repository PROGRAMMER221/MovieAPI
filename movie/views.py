from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import MovieSerializer
from .models import Movie
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/get-movie/',
		'Create':'/post-movie/',
        'Update' : '/update-movie/'
		}

	return Response(api_urls)

@api_view(['GET'])
def AllMovie(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def GetMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=movie)

    return Response(serializer.data)

@api_view(['POST'])
def PostMovie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    print(movie)
    serializer = MovieSerializer(instance=movie, data=request.data)

    if serializer.is_valid():
        print('SAVING')
        serializer.save()
    else: 
        print('NO SAVING')

    return Response(serializer.data)