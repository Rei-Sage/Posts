import django_filters

from news.models import *
from django.db.models import ImageField


class ProductFilter(django_filters.FilterSet):

    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), field_name='category')

    class Meta:
        model = Post
        exclude = ['image']
    filter_overrides = {
            ImageField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {'lookup_expr': 'icontains'}, 
            },
        }
