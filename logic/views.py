from rest_framework import viewsets
from .models import ExampleModel
from .serializers import ExampleSerializer

class ExampleViewSet(viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer
