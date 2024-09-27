from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Account, Bank
from .serializers import AccountSerializer,BankSerializer
from rest_framework.response import Response

# Create your views here.
class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class BankApiView(GenericAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get(self,request):
        bank_objs = Bank.objects.all()
        serializer = BankSerializer(bank_objs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)