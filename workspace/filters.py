
from django import forms 
from news.models import *

import django_filters


import django_filters
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Название",
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-700 text-white border-none p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300',
            'placeholder': 'Введите название',
            'style': 'box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);',
        })
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="Все категории",
        label="Категория",
        widget=forms.Select(attrs={
            'class': 'bg-gray-700 text-white border-none p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300',
            'style': 'box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);',
        })
    )
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        label="Дата",
        widget=django_filters.widgets.RangeWidget(attrs={
            'class': 'bg-gray-700 text-white border-none p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300',
            'placeholder': 'YYYY-MM-DD',
            'style': 'box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);',
        })
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Post.objects.first().tags.all(),
        label="Теги",
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'bg-gray-700 text-white p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300',
            'style': 'box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);',
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'created_at', 'tags', 'views']
