from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #score = serializers.HyperlinkedRelatedField(many=True, view_name='score-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 
            'id', 
            'username',  
            ) 