from rest_framework import permissions
from rest_framework import viewsets

from score.models import Score
from score.serializers import ScoreSerializer
from score.permissions import IsOwnerOrReadOnly

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ScoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    )
    permission_classes = (IsAuthenticated,)
