from rest_framework import serializers
from score.models import Score
from user.models import User


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Score
        fields = (
            'url', 
            'id', 
            'user',
            'score', 
            'date', 
            'username',
            )