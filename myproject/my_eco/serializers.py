from rest_framework import serializers
from .models import Statements


class StatementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statements
        fields = ('id', 'date', 'amount', 'type', 'purpose', 'balance')