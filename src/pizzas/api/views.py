from rest_framework import generics
from django.http import HttpResponse
from ..models import Pizza, Size, Topping
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    PizzaSerializer,
    SizeSerializer,
    ToppingSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class PizzaListCreateView(generics.ListCreateAPIView):
    """
    This view handles the creating and listing of Pizzas
    """

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("topping", "size")

    def create(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SizeListCreateView(generics.ListCreateAPIView):
    """
    This view handles the creating and listing of Pizzas
    """

    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def create(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToppingListCreateView(generics.ListCreateAPIView):
    """
    This view handles the creating and listing of Toppings
    """

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    def create(self, request):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaUpdateRetriveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view handles the updating, retrieving and deletion of Pizzas
    """

    qs = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = "id"

    def retrieve(self, request, pk):
        try:
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            return HttpResponse(status.HTTP_404_NOT_FOUND)

        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            return HttpResponse(status.HTTP_404_NOT_FOUND)

        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
