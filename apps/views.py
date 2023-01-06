from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets

from apps.documents import ArticleDocument
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION

from apps.models import Article
from apps.serializers import ArticleDocumentSerializer, ArticleSerializer


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


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search = self.request.query_params.get("search")
        qs = Article.objects.all()
        if search:
            s = ArticleDocument.search().query("match", title=search)[:5]
            qs = s.to_queryset()
        return qs