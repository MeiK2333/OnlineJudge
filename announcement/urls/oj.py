from django.conf.urls import url

from ..views.oj import AnnouncementAPI, CarouselAPI, FriendshipLinksAPI

urlpatterns = [
    url(r"^announcement/?$", AnnouncementAPI.as_view(), name="announcement_api"),
    url(r"^carousel/?$", CarouselAPI.as_view(), name="carousel_api"),
    url(r"^friendship_links/?$", FriendshipLinksAPI.as_view(), name="friendship_links"),
]
