from utils.api import APIView

from announcement.models import Announcement, Carousel, FriendshipLinks
from announcement.serializers import AnnouncementSerializer, CarouselSerializer, FriendshipLinksSerializer
from django.db.models import Q


class AnnouncementAPI(APIView):
    def get(self, request):
        announcements = Announcement.objects.filter(visible=True)
        keyword = request.GET.get("keyword", "").strip()
        announcements = announcements.filter(Q(title__icontains=keyword))
        return self.success(self.paginate_data(request, announcements, AnnouncementSerializer))


class CarouselAPI(APIView):
    def get(self, request):
        carousels = Carousel.objects.filter(visible=True)
        return self.success(CarouselSerializer(carousels, many=True).data)


class FriendshipLinksAPI(APIView):
    def get(self, request):
        friendship_links = FriendshipLinks.objects.filter(visible=True)
        return self.success(FriendshipLinksSerializer(friendship_links, many=True).data)
