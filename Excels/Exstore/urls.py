from django.conf.urls import url
from .views import UserDataList

urlpatterns = [
    url(r'^', UserDataList.as_view(), name='list'),
]