from rest_framework import serializers
from django.utils import timezone
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def validate_date(self, value):
        """
        Verifica se a data de realização da atividade é
        anterior à data atual.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError("The date cannot be in the past.")
        return value

    def validate_title(self, value):
        """
        Verifica se o título da atividade tem mais de 3 caracteres.
        """
        if len(value) < 3:
            raise serializers.ValidationError("The title must have at least 3 characters.")
        return value
