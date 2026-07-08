from django.contrib.auth import get_user_model
from typing import TYPE_CHECKING

User = get_user_model()

if TYPE_CHECKING:
  from .models import User

def create(*, user: dict) -> 'User':
  user = User.objects.create_user(**user)
  return user

def update(user: 'User', **kwargs) -> 'User':
  for attr, value in kwargs.items():
    setattr(user, attr, value)
  user.save()
  return user

def delete(user: 'User') -> None:
  user.delete()
