from rest_framework import serializers
import uuid
from utils.main import base64_to_image_file
from news.models import *
import django_filters
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at', 'views', 'ratings'] 


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(label='Пароль',write_only=True, min_length=4,)
    password2 = serializers.CharField(label='Подверждение пароль',write_only=True, min_length=4)
    first_name=serializers.CharField(label='Имя', min_length=2)
    last_name=serializers.CharField(label='Фамилия', min_length=4)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'role','phone_number', 'gender', 'race', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают 002!")
        return data


    def create(self, validated_data):
        validated_data.pop('password2') 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            gender=validated_data.get('gender'),
            race=validated_data.get('race'),
            password=validated_data['password1'],
            first_name=validated_data.get("first_name",""),
            last_name=validated_data.get("last_name", ""),
            role=validated_data.get('role',"")
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label='Имя')
    password = serializers.CharField(label="Пароль",write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Неверные данные уч записи")

        refresh = RefreshToken.for_user(user)
        return {
            'username': data['username'],
            'password': data['password'],
            'refresh новый токен для accessы': str(refresh),
            'access данный токен.': str(refresh.access_token),
        }


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avatar
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    image=AvatarSerializer()
    class Meta:
        model=User
        fields=('id','username','first_name','last_name','password','image')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'



class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
    category=CategorySerializer()
    tags=TagSerializer(many=True)
    author=AuthorSerializer()


class DetailPostSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    tags=TagSerializer(many=True)
    author=AuthorSerializer()
    image=serializers.CharField(required=False)
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(source='image')
    image=serializers.CharField(required=False)
    # image = serializers.ListSerializer(child=serializers.CharField())
    class Meta:
        model = Post
        fields = '__all__'
    
    
class UpdatesSerializer(serializers.ModelSerializer):
    image=serializers.CharField()

    class Meta:
        model = Post
        fields = '__all__'

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


