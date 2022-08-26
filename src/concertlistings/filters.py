import django_filters
from .models import *


class ListingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='iexact')

    class Meta:
        model = Concert
        fields = ['artist', 'venue', 'date', 'genre', 'price']
