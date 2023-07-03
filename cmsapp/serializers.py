from rest_framework import serializers
from .models import User,Post_blog,Like


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.ReadOnlyField()
    class Meta:
        model = Post_blog
        fields = "__all__"

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    like_id = serializers.ReadOnlyField()
    class Meta:
        model = Like
        fields = "__all__"