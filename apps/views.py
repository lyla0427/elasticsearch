from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from apps.documents import ArticleDocument
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from apps.serializers import ArticleDocumentSerializer


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
        SuggesterFilterBackend
    ]

    search_fields = ('title',)
    filter_fields = {'category': 'category.id'}
    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }