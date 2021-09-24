from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .models import Statements
from .serializers import StatementsSerializer
from django.http import HttpResponse


class StatementsViewSet(ModelViewSet):
    serializer_class = StatementsSerializer

    def get_object(self):
        return get_object_or_404(Statements, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Statements.objects.all()

    def perform_destroy(self, instance):
        instance.save()


def index(request):
    statements = Statements.objects.all()
    return render(request, 'index.html', {'statements': statements})