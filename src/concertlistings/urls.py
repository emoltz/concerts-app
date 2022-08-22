from django.urls import path

from .views import (
    ConcertListView,
    ConcertDetailView
)


app_name = 'concerts'
urlpatterns = [
    path('', ConcertListView.as_view(), name='concert-list'),
    path('<int:id>/', ConcertDetailView.as_view(), name='concert-detail')
]
