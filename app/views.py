from django.shortcuts import render
from .models import Fish,Order
from .serializers import FishSerializer,OrderSerializer

from rest_framework .response import Response
from rest_framework .views import APIView
from rest_framework . permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly


# Create your views here.

    
class Home(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        fish = Fish.objects.all()
        serializer = FishSerializer(fish,many=True)
        return Response(
            serializer.data
        )
    
class Single(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        fish = Fish.objects.get(id=id)
        serializer = FishSerializer(fish)
        return Response(
            serializer.data
        )
    
class OrderFish(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id):
        quantity = request.data.get('quantity')
        order = Fish.objects.get(id=id)
        data = {
            "user":request.user.id,
            "name":order.name,
            "quantity":quantity,
            "price":order.price
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Order palced"
                }
            )
        return Response(
                serializer.errors
            )
    
class MyOrder(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        order = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(order,many=True)
        return Response(
            serializer.data
        )

class Search(APIView):
    def get(self,request):
        search = request.data.get('search')
        if search:
            queryset = Fish.objects.filter(name__icontains=search)
            if queryset.count()==0:
                return Response(
                    {'message':'no result found'}
                    )
            else:
                serializer = FishSerializer(queryset,many=True)
                return Response(serializer.data)
   
    
class AdminHome(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self,request):
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                'message':'Created'
                }
            )
        return Response(
            serializer.errors
        )
    
class AdminEdit(APIView):
    permission_classes = [IsAdminUser]
    def put(self,request,id):
        fish = Fish.objects.get(id=id)
        serializer = FishSerializer(fish,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"updated"
                }
            )
        return Response(
            serializer.errors
        )
    
class AdminViewOrder(APIView):
    def get(self,request):
        orders = Order.objects.all()
        data = {

        }
        serializer =OrderSerializer(orders,many=True)
        return Response(
            serializer.data
        )
    
