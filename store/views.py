from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import *
from store.models import *


@api_view(['GET'])
def customerlist(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializers(customer, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def customercreate(request):
    serializer = CustomerSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def customerupdate(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializers(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def customerdelete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def productlist(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def productcreate(request):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def productupdate(request, pk):
    produc = Product.objects.get(id=pk)
    serializer = ProductSerializers(instance=produc, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def productdelete(request, pk):
    produc = Product.objects.get(id=pk)
    produc.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def orderlist(request):
    order = Order.objects.all()
    serializer = OrderSerializers(order, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def ordercreate(request):
    serializer = OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def orderupdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializers(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def orderdelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def orderItemlist(request):
    orderItem = OrderItem.objects.all()
    serializer = OrderItemSerializers(orderItem, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def orderItemcreate(request):
    serializer = OrderItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def orderItemupdate(request, pk):
    orderItem = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializers(instance=orderItem, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def orderItemdelete(request, pk):
    orderItem = OrderItem.objects.get(id=pk)
    orderItem.delete()
    return Response('Item succsesfuly deleted')


@api_view(['GET'])
def shippingAddresslist(request):
    shippingAddress = ShippingAddress.objects.all()
    serializer = ShippingAddressSerializers(shippingAddress, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def shippingAddressreate(request):
    serializer = ShippingAddressSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def shippingAddressupdate(request, pk):
    shippingAddress = ShippingAddress.objects.get(id=pk)
    serializer = ShippingAddressSerializers(
        instance=shippingAddress, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def shippingAddressdelete(request, pk):
    shippingAddress = ShippingAddress.objects.get(id=pk)
    shippingAddress.delete()
    return Response('Item succsesfuly deleted')
