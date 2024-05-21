from django.shortcuts import render
from rest_framework import permissions, viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .models import BeerModel
from .serializers import BeerSerializer


class BeerView(viewsets.ModelViewSet):
    queryset = BeerModel.objects.all().order_by('name')
    serializer_class = BeerSerializer
    permission_classes = [permissions.IsAuthenticated]

