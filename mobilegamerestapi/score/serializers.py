from rest_framework import serializers
from score.models import Score

"""
class ScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    score = serializers.IntegerField()

    def create(self, validated_data):
        return Score.objects.create(**validated_data)
"""

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'name', 'score', 'date',)