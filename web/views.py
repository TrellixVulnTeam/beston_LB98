from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import IncomeSerializers, ExpenseSerializers
from web.models import *


@api_view(['GET'])
def expenselist(request):
    expense = Expense.objects.all()
    serializer = ExpenseSerializers(expense, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def incomeelist(request):
    income = Income.objects.all()
    serializer = IncomeSerializers(income, many=True)
    return Response(serializer.data)
