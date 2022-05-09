from django.conf.urls import url

from ..views.admin import AnnouncementAdminAPI, CarouselAdminAPI, FriendshipLinksAdminAPI

urlpatterns = [
    url(r"^announcement/?$", AnnouncementAdminAPI.as_view(), name="announcement_admin_api"),
    url(r"^carousel/?$", CarouselAdminAPI.as_view(), name="carousel_api"),
    url(r"^friendship_links/?$", FriendshipLinksAdminAPI.as_view(), name="friendship_links"),
]
