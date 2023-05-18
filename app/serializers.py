from rest_framework import serializers
from .models import Fish,Order

class FishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fish
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        

