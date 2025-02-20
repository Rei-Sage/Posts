from pprint import pprint
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from api.serializers import *
from news.models import *
from api.filters import ProductFilter
from api.permissions import IsAdminOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from api.paginations import SimplePagination
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsSalesmanOrReadOnly, IsSalesman, IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from api.mixins import SuperGenericAPIView, UltraModelViewSet


User = get_user_model()


class PostViewSet(UltraModelViewSet):
    queryset = Post.objects.all()
    serializer_classes = {
        'list': ListPostSerializer,
        'retrieve': DetailPostSerializer,
        'create': CreatePostSerializer,
        'update': UpdatesSerializer,
    }
    pagination_class = SimplePagination
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ['title', ]
    ordering_fields = ['views', 'title']
    filterset_class = ProductFilter
    permission_classes_by_action = {
        'list':  [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSalesman],
        'update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner],
    }



class AvatarViewSet(UltraModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    lookup_field = 'id'

class CategoryViewSet(UltraModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class TagViewSet(UltraModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'
    
class RegisterView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

