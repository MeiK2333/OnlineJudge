from account.decorators import super_admin_required, super_admin_or_secondary_required
from announcement.models import Announcement, Carousel, FriendshipLinks
from announcement.serializers import (AnnouncementSerializer, CreateAnnouncementSerializer,
                                      EditAnnouncementSerializer, CarouselSerializer, CreateCarouselSerializer,
                                      EditCarouselSerializer, CreateFriendshipLinksSerializer,
                                      EditFriendshipLinksSerializer, FriendshipLinksSerializer)
from utils.api import APIView, validate_serializer


class AnnouncementAdminAPI(APIView):
    @validate_serializer(CreateAnnouncementSerializer)
    @super_admin_or_secondary_required
    def post(self, request):
        """
        publish announcement
        """
        data = request.data
        verify = True
        if request.user.is_secondary_admin():
            verify = False
        announcement = Announcement.objects.create(title=data["title"],
                                                   content=data["content"],
                                                   created_by=request.user,
                                                   visible=data["visible"],
                                                   order=data["order"],
                                                   verify=verify)
        return self.success(AnnouncementSerializer(announcement).data)

    @super_admin_required
    def put(self, request):
        """
        edit announcement
        """
        data = request.data
        try:
            announcement = Announcement.objects.get(id=data.pop("id"))
        except Announcement.DoesNotExist:
            return self.error("Announcement does not exist")

        for k, v in data.items():
            setattr(announcement, k, v)
        announcement.save()

        return self.success(AnnouncementSerializer(announcement).data)

    @super_admin_or_secondary_required
    def get(self, request):
        """
        get announcement list / get one announcement
        """
        announcement_id = request.GET.get("id")
        if announcement_id:
            try:
                announcement = Announcement.objects.get(id=announcement_id)
                return self.success(AnnouncementSerializer(announcement).data)
            except Announcement.DoesNotExist:
                return self.error("Announcement does not exist")
        announcement = Announcement.objects.all()
        if request.GET.get("visible") == "true":
            announcement = announcement.filter(visible=True)
        return self.success(self.paginate_data(request, announcement, AnnouncementSerializer))

    @super_admin_required
    def delete(self, request):
        if request.GET.get("id"):
            Announcement.objects.filter(id=request.GET["id"]).delete()
        return self.success()

class CarouselAdminAPI(APIView):
    @validate_serializer(CreateCarouselSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        carousel = Carousel.objects.create(title=data["title"], visible=data["visible"], order=data["order"],
                                           file_path=data["file_path"], created_by=request.user)
        return self.success(CarouselSerializer(carousel).data)

    @validate_serializer(EditCarouselSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            carousel = Carousel.objects.get(id=data.pop("id"))
        except Carousel.DoesNotExist:
            return self.error("Announcement does not exist")

        for k, v in data.items():
            setattr(carousel, k, v)
        carousel.save()

        return self.success(CarouselSerializer(carousel).data)

    @super_admin_required
    def get(self, request):
        carousel_id = request.GET.get("id")
        if carousel_id:
            try:
                carousel = Carousel.objects.get(id=carousel_id)
                return self.success(CarouselSerializer(carousel).data)
            except Carousel.DoesNotExist:
                return self.error("Carousel does not exist")

        carousels = Carousel.objects.all().order_by("-order")
        return self.success(CarouselSerializer(carousels, many=True).data)

    @super_admin_required
    def delete(self, request):
        Carousel.objects.filter(id=request.GET["id"]).delete()
        return self.success()


class FriendshipLinksAdminAPI(APIView):
    @validate_serializer(CreateFriendshipLinksSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        friendship_links = FriendshipLinks.objects.create(title=data["title"], visible=data["visible"],
                                                          order=data["order"],
                                                          link=data["link"], created_by=request.user)
        return self.success(FriendshipLinksSerializer(friendship_links).data)

    @validate_serializer(EditFriendshipLinksSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            friendship_links = FriendshipLinks.objects.get(id=data.pop("id"))
        except FriendshipLinks.DoesNotExist:
            return self.error("Announcement does not exist")

        for k, v in data.items():
            setattr(friendship_links, k, v)
        friendship_links.save()

        return self.success(FriendshipLinksSerializer(friendship_links).data)

    @super_admin_required
    def get(self, request):
        friendship_links_id = request.GET.get("id")
        if friendship_links_id:
            try:
                friendship_links = FriendshipLinks.objects.get(id=friendship_links_id)
                return self.success(FriendshipLinksSerializer(friendship_links).data)
            except FriendshipLinks.DoesNotExist:
                return self.error("Carousel does not exist")

        friendship_links = FriendshipLinks.objects.all().order_by("-order")
        return self.success(FriendshipLinksSerializer(friendship_links, many=True).data)

    @super_admin_required
    def delete(self, request):
        FriendshipLinks.objects.filter(id=request.GET["id"]).delete()
        return self.success()
