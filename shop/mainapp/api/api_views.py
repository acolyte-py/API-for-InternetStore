from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .serializer import (
    CategorySerializer,
    SmartphoneSerializer,
    NotebookSerializer,
)
from ..models import Category, Smartphone, Notebook


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.object.all()


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title', 'accum_volume']


class NotebookListAPIView(ListAPIView):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title', 'video']
