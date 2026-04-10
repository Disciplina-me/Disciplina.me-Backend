from django.db.models import QuerySet
from .models import Activity

def activity_list() -> QuerySet[Activity]:
  """
  Retorna a queryset para as atividades
  """
  return Activity.objects.all()
