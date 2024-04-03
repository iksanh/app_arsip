from django.contrib.auth.models import Group


def add_user_group(groupname, user):
  my_group = Group.objects.get(name=f'{groupname}') 
  my_group.user_set.add(user)