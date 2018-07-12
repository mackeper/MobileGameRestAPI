from score.models import Score
from score.serializers import ScoreSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from score.serializers import UserSerializer
from rest_framework import permissions
from score.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets

class ScoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
                          
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'score': reverse('score-list', request=request, format=format)
    })