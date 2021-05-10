from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .serializer import (
    CategorySerializer,
    SmartphoneSerializer,
    NotebookSerializer,
    CustomerSerializer,
)
from ..models import Category, Smartphone, Notebook, Customer


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


class SmartphoneDetailAPIView(RetrieveAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    lookup_field = 'id'


class NotebookDetailAPIView(RetrieveAPIView):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    lookup_field = 'id'


class CustomersListAPIView(ListAPIView):
    """Это для практики, в реале такой функционал делать не стоит"""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

