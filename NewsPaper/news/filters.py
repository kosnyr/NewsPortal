from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dataCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%M-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'postCategory'
        ]

        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'postCategory': 'Категория'
        }
