from django.urls import path

from .views import (
    concert_list_view,
    concert_detail_view,
    ConcertListView,
    ConcertDetailView,
)


app_name = 'concerts'
urlpatterns = [
    path('', concert_list_view, name='concert-list'),
    path('<str:id>/', concert_detail_view, name='concert-detail')
    # path('G5vVZ9dLbWv5L/', concert_detail_view, name='concert-detail')
]
