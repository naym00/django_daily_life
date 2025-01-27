from rest_framework import serializers
from user import models as M_USER

class Usersrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_USER.User
        fields=['id', 'phone', 'gender']

class Profilepicsrlzr(serializers.ModelSerializer):
    user=Usersrlzr(many=False)
    class Meta:
        model=M_USER.Profilepic
        fields=['id', 'user', 'image', 'is_active']
        
class Coverphotosrlzr(serializers.ModelSerializer):
    user=Usersrlzr(many=False)
    class Meta:
        model =M_USER.Coverphoto
        fields=['id', 'user', 'image', 'is_active']