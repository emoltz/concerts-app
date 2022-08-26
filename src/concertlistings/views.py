from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    ListView,
    DetailView
)

from .util.api_service import ApiService

from .models import Concert

api_service = ApiService()


class ConcertListView(ListView):
    template_name = 'concert_list.html'
    queryset = api_service.get_concerts()
    # queryset = Concert.objects.all()


class ConcertDetailView(DetailView):
    template_name = 'concert_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Concert, id=id_)
