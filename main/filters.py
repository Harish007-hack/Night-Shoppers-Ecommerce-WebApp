from django_filters import FilterSet
from django.db.models import Q
import django_filters
from .models import *

class SearchFilter(FilterSet):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['Image','user']

class LocationFilter(FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', label="Search")

    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['Image','user','date_created','description']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(loc__icontains=value) | Q(loc_mansioned__icontains=value) | Q(loc_country__icontains=value) | Q(loc_modern__icontains=value)
        )