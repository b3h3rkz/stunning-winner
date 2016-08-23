from django.conf.urls import url
from .views import UserDataList, save_to_db

urlpatterns = [
    url(r'^$', UserDataList.as_view(), name='list'),
    url(r'^upload/$', save_to_db, name='upload'),
]