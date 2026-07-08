from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from typing import TYPE_CHECKING

User = get_user_model()

#Essa condicão só esta sendo usada pelo fato do nosso model customizado de usuário se chamar User
#Dessa forma, para validar a diferenciacao da variavel para o tipo de retorno, usamos o TYPE_CHECKING
if TYPE_CHECKING:
  from .models import User

def get_user_by_id(*, user_id: str) -> 'User':
  try:
    user = User.objects.get(id=user_id)
    return user
  except Exception as e:
    return None

def get_users() -> QuerySet['User']:
  return User.objects.all()
