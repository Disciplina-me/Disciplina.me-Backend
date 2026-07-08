from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'age', 'institution_name']
    read_only_fields = ['id']

  def validate_phone(self, value):
    if value and len(value) != 11:
      raise serializers.ValidationError("Phone number must be 11 digits long.")
    return value
