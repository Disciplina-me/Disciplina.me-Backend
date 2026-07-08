from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from . import selectors
from . import services

class UsersViewSet(viewsets.ViewSet):

    def list(self, request):
      queryset = selectors.get_users()
      serializer = UserSerializer(queryset, many=True)
      return Response(serializer.data)

    def create(self, request):
      serializer = UserSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = services.create(user=serializer.validated_data)
      return Response(UserSerializer(user).data, status=201)

    def retrieve(self, request, pk=None):
      user = selectors.get_user_by_id(user_id=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)

    def update(self, request, pk=None):
      user = selectors.get_user_by_id(pk)
      serializer = UserSerializer(user, data=request.data)
      serializer.is_valid(raise_exception=True)
      user = services.update(user, **serializer.validated_data)
      return Response(UserSerializer(user).data)

    def destroy(self, request, pk=None):
      user = selectors.get_user_by_id(pk)
      services.delete(user)
      return
