from rest_framework.response import Response


def isInGroup(groupname):
  def _inner_func(function):
    def _inner(request, *args, **kwargs):
      if request.user.groups.filter(name__in = groupname).exists():
        return function(request, *args, **kwargs)
      return Response('Wrong Permissions',status=400)
    return _inner
  return _inner_func