from rest_framework.serializers import ModelSerializer
from .models import Account,Bank

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'