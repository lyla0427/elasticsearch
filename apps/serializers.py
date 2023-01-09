from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from apps.documents import ArticleDocument
from apps.models import Article


class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument

        fields = (
            'id',
            'title',
            'category'
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = (
            'id',
            'title',
            'category'
        )