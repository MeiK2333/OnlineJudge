from django.conf.urls import url

from ..views.oj import AnnouncementAPI, CarouselAPI

urlpatterns = [
    url(r"^announcement/?$", AnnouncementAPI.as_view(), name="announcement_api"),
    url(r"^carousel/?$", CarouselAPI.as_view(), name="carousel_api"),
]
