from rest_framework import permissions
from rest_framework import viewsets

from score.models import Score
from score.serializers import ScoreSerializer
from score.permissions import IsOwnerOrReadOnly


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