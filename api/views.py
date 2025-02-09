from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from goods.models import Goods


@api_view(['GET', 'POST'])
def goods_list(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        serializer = serializers.GoodSerializer(goods, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET', 'PUT', 'DELETE'])
def goods_detail(request, pk):
    try:
        goods = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.GoodSerializer(goods)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.GoodSerializer(goods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)