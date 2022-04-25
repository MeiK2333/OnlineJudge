from utils.api import APIView

from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer
from django.db.models import Q


class AnnouncementAPI(APIView):
    def get(self, request):
        announcements = Announcement.objects.filter(visible=True)
        keyword = request.GET.get("keyword", "").strip()
        announcements = announcements.filter(Q(title__icontains=keyword))
        return self.success(self.paginate_data(request, announcements, AnnouncementSerializer))
