from django.conf.urls import url
from .views import UserDataList, save_to_db, LogView

urlpatterns = [
    url(r'^$', UserDataList.as_view(), name='list'),
    url(r'^upload/$', save_to_db, name='upload'),
    url(r'^logs/$', LogView.as_view(), name='logs'),
]