from rest_framework.generics import ListAPIView

from .serializer import CategorySerializer
from ..models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.object.all()

