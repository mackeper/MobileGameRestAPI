from rest_framework import serializers
from score.models import Score
from django.contrib.auth.models import User


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Score
        fields = ('url', 'id', 'name', 'score', 'date', 'owner',)