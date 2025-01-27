from rest_framework import serializers
from user import models as M_USER

class Usersrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_USER.User
        fields='__all__'

class Profilepicsrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_USER.Profilepic
        fields='__all__'
        
class Coverphotosrlzr(serializers.ModelSerializer):
    class Meta:
        model =M_USER.Coverphoto
        fields='__all__'