from rest_framework import serializers
import uuid
from utils.main import base64_to_image_file
from news.models import *

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avatar
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(source='image.image')
    image=AvatarSerializer()
    class Meta:
        model=User
        fields=('id','username','first_name','last_name','password','image')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'



class ListPostSerializer(serializers.ModelSerializer):
    # category=serializers.CharField(source='category.name')
    # image = serializers.ImageField(source='image')
    # category = serializers.CharField(source='category.name') 
    # tags = serializers.ListSerializer(child=serializers.CharField(source='tags.name'))

    # image=serializers.ImageField(source='post.image')
    # ava=AvatarSerializer(many=True)

    # image=serializers.ImageField(source='ava.image')
  
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
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(source='image')
    image=serializers.CharField()
    # image = serializers.ListSerializer(child=serializers.CharField())
    class Meta:
        model = Post
        fields = '__all__'
    
    def create(self,validated_data):
        image = validated_data.pop('image',None)
        tags = validated_data.pop('tags')
        if image:
            try:
                file = base64_to_image_file(image, uuid.uuid4())
            except Exception as e:
                print(e)
                raise serializers.ValidationError(
                    {'image': ['Загрузите корректное изображение']}
                )
        post = Post.objects.create(**validated_data)
        post.tags.add(*tags)

        if image:
            post.image.save(file.name, file)
        return post
    
class UpdatesSerializer(serializers.ModelSerializer):
    image=serializers.CharField()

    class Meta:
        model = Post
        fields = '__all__'
    
    def update(self,instance,validated_data):
        image = validated_data.pop('image', None) 
        tags = validated_data.pop('tags')
        return instance
    





        # for image in image:
        #     try:
        #         file = base64_to_image_file(image, uuid.uuid4())
        #         file_images.append(file)
        #     except Exception as e:
        #         print(e)
        #         raise serializers.ValidationError(
        #             {'images': ['Загрузите корректное изображение']}
        #         )

        # for file_image in file_images:
        #     post_image = Post.objects.get(id=post.id)
        #     post_image.image.save(file_image.name, file_image)
        #     post_image.save()


