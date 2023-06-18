from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from rest_framework import viewsets
from apps.diets.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_vector = SearchVector("name", "brand")
        search_query = SearchQuery(query)
        queryset = Product.objects.annotate(
            search=search_vector, rank=SearchRank(search_vector, search_query)
        ).filter(search=search_query).order_by("-rank")
        return queryset
