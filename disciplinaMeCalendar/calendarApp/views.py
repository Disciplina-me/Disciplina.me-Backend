from rest_framework import generics
from .serializers import ActivitySerializer
from . import services
from . import selectors


class ActivityListCreateView(generics.ListCreateAPIView):
    """
    Todas essas requisições vão funcionar no endpoint /activities
    """
    serializer_class = ActivitySerializer

    #Faz um POST automaticamente
    def perform_create(self, serializer):
        services.activity_create(validated_data=serializer.validated_data)

    #Faz um GET automaticamente
    def get_queryset(self):
        return selectors.activity_list()

class ActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Todas as requisições irão funcionar no endpoint /activities/<id>.
    """
    serializer_class = ActivitySerializer

    def get_queryset(self):
       return selectors.activity_list()

    #Faz um PUT automaticamente
    def perform_update(self, serializer):
      services.activity_update(instance=serializer.instance, validated_data=serializer.validated_data)

    #Faz um DELETE automaticamente
    def perform_destroy(self, instance):
      services.activity_delete(instance=instance.id)
