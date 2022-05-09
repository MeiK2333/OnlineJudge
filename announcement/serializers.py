from utils.api import serializers
from utils.api._serializers import UsernameSerializer

from .models import Announcement, Carousel, FriendshipLinks


class CreateAnnouncementSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    visible = serializers.BooleanField()
    order = serializers.IntegerField()


class AnnouncementSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer()

    class Meta:
        model = Announcement
        fields = "__all__"


class EditAnnouncementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    visible = serializers.BooleanField()
    order = serializers.IntegerField()


class CreateCarouselSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    visible = serializers.BooleanField()
    file_path = serializers.CharField(max_length=128)
    order = serializers.IntegerField()


class EditCarouselSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    visible = serializers.BooleanField()
    file_path = serializers.CharField(max_length=128)
    order = serializers.IntegerField()


class CarouselSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer()

    class Meta:
        model = Carousel
        fields = "__all__"


class CreateFriendshipLinksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    visible = serializers.BooleanField()
    link = serializers.CharField(max_length=512)
    order = serializers.IntegerField()


class EditFriendshipLinksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    visible = serializers.BooleanField()
    link = serializers.CharField(max_length=512)
    order = serializers.IntegerField()


class FriendshipLinksSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer()

    class Meta:
        model = FriendshipLinks
        fields = "__all__"
