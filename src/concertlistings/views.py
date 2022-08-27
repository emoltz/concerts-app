from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)

from .util.api_service import ApiService
from .filters import *

from .models import Concert

api_service = ApiService()


def concert_list_view(request):
    queryset = api_service.get_concerts()
    context = {
        'object_list': queryset
    }
    return render(request, 'concert_list.html', context=context)


def concert_detail_view(request, id, *args, **kwargs):
    context = {
        "concert": api_service.get_concert_by_id(id)
    }
    return render(request, 'concert_detail.html', context=context)


class ConcertListView(ListView):
    template_name = 'concert_list.html'
    queryset = api_service.get_concerts()
    # queryset = Concert.objects.all()
    listing_filter = ListingFilter()  # this is from the `django-filters` package but I'm not sure how to use it yet


class ConcertDetailView(DetailView):
    template_name = 'concert_detail.html'
    context_object_name = 'concert'
    # TODO is this right?? How to do a class based endering of the above function concert_detail_view?

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Concert, id=id_)
