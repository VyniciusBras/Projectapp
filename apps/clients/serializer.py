from .models import Client, ClientSocialnetwork
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '_all_'
        
class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialnetwork
        fields = '_all_'