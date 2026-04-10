from .models import Activity

#O asterisco força a função a lidar com parâmetros nomeados
def activity_create(*, validated_data:dict) -> Activity:
  activity = Activity.objects.create(**validated_data)
  return activity

def activity_update(*, instance:Activity, validated_data:dict) -> Activity:
  for attr, value in validated_data.items():
    setattr(instance, attr, value)
  instance.save()
  return instance


def activity_delete(*, instance: Activity) -> Activity:
  instance.delete()
