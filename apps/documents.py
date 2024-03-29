from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from .models import Article


nori_tokenizer = analyzer(
    'nori_tokenizer',
    tokenizer='nori_tokenizer',
)


@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(analyzer= nori_tokenizer, attr='title', fields={'raw': fields.TextField(), 'suggest': fields.CompletionField()})
    category = fields.ObjectField(attr='category', properties={'id': fields.IntegerField(), 'title': fields.TextField(attr='title', fields={'raw': fields.KeywordField()})})

    class Index:
        name = 'articles'

    class Django:
        model = Article
