from pprint import pprint

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from api.serializers import *
from news.models import *

@api_view(['PUT'])
def update(request,id):
    if request.method=='PUT':
        instance=Post.objects.get(id=id)
        serializer=UpdatesSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            post=serializer.save()
            read_serializer = DetailPostSerializer(post, context={'request': request})
            return Response(read_serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.all()
    serializer = ListPostSerializer(posts, many=True,context={'request':request})
    return Response(serializer.data)


@api_view(['GET','POST','PUT'])
def list_posts(request):
    if request.method=='POST':
        serializer=CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            post=serializer.save()
            read_serializer = DetailPostSerializer(post, context={'request': request})
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.all()
    serializer = ListPostSerializer(posts, many=True,context={'request':request})
    return Response(serializer.data)


@api_view(['GET'])
def detail_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = DetailPostSerializer(post,context={'request':request})
    return Response(serializer.data)